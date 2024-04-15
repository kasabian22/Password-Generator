from flask import Flask, render_template, request
from flask_session import Session
from helpers import apology, generate_password

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        password = generate_password()
        return render_template("homepage.html", password=password)
    else:
        return render_template("homepage.html")

@app.route("/password", methods=["POST", "GET"])
def password():
    if request.method == "POST":
        if not any(request.form.getlist(key) for key in ['upper_case', 'lower_case', 'symbols', 'numbers']):
            return apology('error: At least one checkbox must be selected', 400)

        length = int(request.form.get("length", 12))
        if length > 50:
            return apology("The Max length is 50", 400)
        elif length < 1:
            return apology("The min length is 1", 400)

        include_uppercase = request.form.get("upper_case", "off") == "on"
        include_lowercase = request.form.get("lower_case", "off") == "on"
        include_symbols = request.form.get("symbols", "off") == "on"
        include_numbers = request.form.get("numbers", "off") == "on"
        password = generate_password(length, include_uppercase, include_lowercase, include_symbols, include_numbers)
        
        return render_template("password.html", password=password)
    else:
        return render_template("password.html", password=None)
    
