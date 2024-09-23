from flask import Flask, render_template, jsonify, request, session, url_for
from messaging_app.func import Database, get_db_name

db = Database(get_db_name())

app = Flask(__name__)
app.secret_key = "secret_key" # not secure lol


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")
    elif request.method == "POST":
        nickname = request.form["nickname"]
        password = request.form["password"]
        if db.if_user_exists(nickname) == True:
            if 
            return render_template()
        else: # if user doesnt exist
            db.create_user(nickname,password)
            session["nickname"] = nickname
            db.log_ip(request.environ['REMOTE_ADDR'],session["nickname"])
            return render_template("main.html")

@app.route("/sendmessage",methods=["POST"])
def send_message():
    user = session["nickname"]
    message = request.form["message"]
    print(user,message)
    db.add_message_to_db(user,message)
    db.log_ip(request.environ['REMOTE_ADDR'],session["nickname"])
    return render_template("main.html")

@app.route("/getmessages",methods=["GET"])
def get_messages():
    messages = db.get_last_messages(20)
    db.log_ip(request.environ['REMOTE_ADDR'],session["nickname"])
    return render_template("messages.html", messages_list=messages)
    
