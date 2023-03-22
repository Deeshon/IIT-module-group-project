import sqlite3
from flask import Flask, request, render_template, session, redirect
from flask_session import Session
from helpers import login_required

#Configure app
app = Flask(__name__)

#Configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

@app.route("/")
@login_required
def home():
   return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        record = [(email)]

        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        try:
            cursor.execute('''SELECT * FROM users where email=?''', record)

            output = cursor.fetchall()
            db_password = output[0][4]

            if password != db_password:
                return render_template("apology.html", message="Password Invalid")
            
            session["user_id"] = output[0][0]

            return redirect("/")
        except:
                return render_template("apology.html", message="User not Registered")
    

    else:
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
    app.run(host="0.0.0.0")
