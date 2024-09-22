from flask import Flask, render_template, jsonify, request
from messaging_app.func import Database, get_db_name

db = Database(get_db_name())

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("main.html")
    
@app.route("/send",methods=["POST"])
def send_message():
    pass