from flask import Flask, render_template, jsonify, request, session, url_for
from messaging_app.func import Database, get_db_name

db = Database(get_db_name())

app = Flask(__name__)
app.secret_key = "secret_key" # not secure lol


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        #previous_20_messages = 
        return render_template("main.html")
    elif request.method == "POST":
        nickname = request.form["nickname"]
        db.create_user(nickname,"")
        session["nickname"] = nickname
        return render_template("main.html")

@app.route("/sendmessage",methods=["POST"])
def send_message():
    user = session["nickname"]
    message = request.form["message"]
    print(user,message)
    db.add_message_to_db(user,message)
    return render_template("main.html")

@app.route("/getmessages",methods=["GET"])
def get_messages():
    messages = db.get_last_messages(20)
    return render_template("messages.html", messages_list=messages)
    
