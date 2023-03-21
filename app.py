import sqlite3
from flask import Flask, request, render_template
from helpers import login_required

app = Flask(__name__)


@app.route("/")
@login_required
def home():
   return render_template("home.html")

@app.route("/login")
def login():
   return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        record = [(name, email, phone, password)]

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO users(name,email,phone,password) VALUES(?,?,?,?)''', record)
        conn.commit()
        conn.close()

        return render_template("login.html")

    else:
        return render_template("register.html")
    
if __name__ == "__main__":
    app.run(debug=True)
