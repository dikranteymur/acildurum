import pymysql


class Database:
    # database name	: "acildurum"
    # tables	    : "users", "events"
    # charset = "utf8"
    # autocommit = True
    # port = 3306
    # unix_socket = "/tmp/mysql.sock"

    def connect_db(self):
        return pymysql.connect(
            host="127.0.0.1",
            user="dikran",
            password="mdt.2000",
            database="acildurum",
            cursorclass=pymysql.cursors.DictCursor)

    def get_all_users(self):
        db = self.connect_db()
        cursor = db.cursor()
        sql = """SELECT * FROM users"""

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except ValueError:
            db.rollback()
            print("HATA VAR")

        db.close()
        return result  # print(type(result)) = <list>

    # func: login
    def login(self, username, password):
        mesaj = ""
        users = self.get_all_users()
        for i in users:
            if i["username"] == username and i["password"] == password:
                print(i["username"])
                print(i["password"])
                mesaj = "{} adlı kullanıcı giriş yaptı".format(username)
                break
            else:
                mesaj = "Yanlış kullanıcı adı veya parola"
        print(mesaj)
        return mesaj

    # func: register
    def register(self, username, password):
        mesaj = ""
        users = self.get_all_users()
        same_user_control = False

        sql = """INSERT INTO users (username, password, kayit_tarihi) VALUES ("{}", "{}", {})""".format(
            username, password, "NOW()")

        if len(users) > 0:
            for i in users:
                if i["username"] == username:
                    print(i["username"])
                    mesaj = "Aynı kullanıcı adı var. Başka bir kullanıcı adı seçiniz"
                    same_user_control = False
                    break
            else:
                same_user_control = True
                print("Kullanıcı kaydedilebilir")

        else:
            print("En alt çalıştı.....Hata")
            self.save_db(username, password, sql)
            mesaj = "{} adlı kullanıcı kaydedildi...".format(username)

        if same_user_control:
            self.save_db(username, password, sql)
            mesaj = "{} adlı kullanıcı kaydedildi...".format(username)
        return mesaj

    def save_db(self, username, password, sqlQuery):
        print("save_db çalıştı......")
        db = self.connect_db()
        cursor = db.cursor()
        try:
            cursor.execute(sqlQuery)
            db.commit()
        except ValueError:
            db.rollback()
            mesaj = "Veritabanına kaydedilemedi"
            return mesaj
        db.close()
