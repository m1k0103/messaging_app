from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def send_message():
    if request.method == "GET":
        return render_template("main.html")
    
    elif request.method == "POST":
        return "posted"

    else:
        return "en error occured"