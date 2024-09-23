import sqlite3
import yaml
import datetime
import time
import random
import string

def get_db_name():
    with open("config.yaml") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        DB_NAME = conf["database_name"]
        return DB_NAME

class Database:
    def __init__(self,database):
        self.database = database

    def add_message_to_db(self,sender,message):
        current_timestamp = time.time()
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO messages(sender_id,message,timestamp) VALUES((SELECT uid FROM userdata WHERE username=?),?,?)", [sender,message,current_timestamp])
        print(f"message from {sender} recieved")
        con.commit()
        con.close()

    def log_ip(self,ip,username):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("UPDATE userdata SET ip=?  WHERE username=?;", [ip,username])
        con.commit()
        con.close()
        print(f"ip of {username} logged: {ip}")

    def create_user(self,username,password):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO userdata(username,password,ip,last_active) VALUES (?,?,?,?)", [username,password,0,0])
        con.commit()
        con.close()
    
    def get_last_messages(self, count):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        result = cursor.execute("SELECT userdata.username,messages.message,messages.timestamp FROM userdata JOIN messages ON messages.sender_id=userdata.uid ORDER BY timestamp ASC LIMIT ?", [count]).fetchall()

        messages = [list(tup) for tup in result] # converts all tuples to lists
        return messages
    
    def if_user_exists(self,nickname):
        con = sqlite3.connect(self.database)
        cursor = con.cursor() # CARRY ON FROM HERE!!!!!

#def populate_messages(db):
#    for i in range(10):
#        db.add_message_to_db(random.choice(["larry", "bob"]),"".join(random.choices(string.ascii_letters, k=5)))

#db = Database(get_db_name())

#db.create_user("larry","betterpassword123")
#db.create_user("bob", "password1234")

#populate_messages(db)
#db.get_last_messages(10)
