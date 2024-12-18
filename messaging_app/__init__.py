import sqlite3
import os
from messaging_app.func import get_db_name

def start():
    DB_NAME = get_db_name()

    if DB_NAME not in os.listdir():
        db = open(f"./{DB_NAME}", "w+")
        db.close()

        con = sqlite3.connect(DB_NAME)
        cursor = con.cursor()
    
        cursor.execute("""CREATE TABLE userdata(
                       uid INTEGER PRIMARY KEY,
                       username TEXT,
                       password TEXT,
                       ip TEXT,
                       last_active TEXT
                       )""")
        cursor.execute("""CREATE TABLE messages(
                       sender_id INT,
                       message TEXT,
                       timestamp FLOAT,
                       FOREIGN KEY(sender_id) REFERENCES userdata(uid)
                       )""")
    
        con.commit()
        con.close()
        print("db created")

    from messaging_app.routes import app
    app.run(host="0.0.0.0",port="80")