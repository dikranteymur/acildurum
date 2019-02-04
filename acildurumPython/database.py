import pymysql


class Database:
    # database name	: "acildurum"
    # tables	    : "users", "events"
    # charset = "utf8"
    # autocommit = True
    # port = 3306
    # unix_socket = "/tmp/mysql.sock"
    mesaj = ""

    def connect_db(self):
        return pymysql.connect(
            host="127.0.0.1", user="dikran", password="mdt.2000", database="acildurum",
            cursorclass=pymysql.cursors.DictCursor)

    def get_all_users(self):
        db = self.connect_db()
        cursor = db.cursor()
        sql = """SELECT * FROM users"""

        try:
            cursor.execute(sql)
            db.commit()
            result = cursor.fetchall()
        except ValueError:
            db.rollback()
            print("HATA VAR")
        db.close()
        return result

    # func: login
    def login(self, username, password):
        mesaj = ""
        users = self.get_all_users()
        for dict in users:
            if dict["username"] == username and dict["password"] == password:
                mesaj = "{} adlı kullanıcı giriş yaptı".format(username)
                print(mesaj)
                return mesaj
            else:
                print(mesaj)
                mesaj = "Yanlış kullanıcı adı veya parola"
                return mesaj

    # func: register
    def register(self, username, password):
        mesaj = ""
        users = self.get_all_users()

        def save_db(username, password, sqlQuery):
            db = self.connect_db()
            cursor = db.cursor()
            try:
                cursor.execute(sqlQuery)
                db.commit()
                mesaj = "{} adlı kullanıcı kaydedildi...".format(
                    username)
                return mesaj
            except ValueError:
                db.rollback()
                mesaj = "Veritabanına kaydedilemedi"
                return mesaj
            db.close()

        sql = """INSERT INTO users (username, password, kayit_tarihi) VALUES ("{}", "{}", {})""".format(
            username, password, "NOW()")

        if len(users) > 0:
            for dict in users:
                if dict["username"] == username:
                    mesaj = "Aynı kullanıcı adı var. Başka bir kullanıcı adı seçiniz"
                    return mesaj
                else:
                    save_db(username, password, sql)
                    mesaj = "{} adlı kullanıcı kaydedildi...".format(
                        username)
                    return mesaj
        else:
            save_db(username, password, sql)
            mesaj = "{} adlı kullanıcı kaydedildi...".format(
                username)
            return mesaj
