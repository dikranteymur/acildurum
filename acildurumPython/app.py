from flask import Flask, request, jsonify, render_template
from database import Database

db = Database()

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    mesajim = "Merhaba! Dünya"
    return render_template("index.html", mesaj=mesajim)


@app.route("/login", methods=["GET", "POST"])
def login():
    mesaj = ""
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        mesaj = db.login(username, password)
    return jsonify({"mesaj": mesaj})
    # return render_template("login.html", username=username, mesaj="Mesaj: Merhaba", content_type="application/json")


@app.route("/register", methods=["GET", "POST"])
def register():
    mesaj = ""
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        print("REGISTER DATA: {}-{}".format(username, password))
        mesaj = db.register(username, password)

    return jsonify({"mesaj": mesaj})


@app.route("/users", methods=["GET", "POST"])
def allUsers():
    result = db.get_all_users()
    return render_template(
        "users.html", result=result, content_type="application/json")


if __name__ == '__main__':
    app.run(debug=True)
