import sqlite3
import yaml
import datetime
import time

def get_db_name():
    with open("config.yaml") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        DB_NAME = conf["database_name"]
        return DB_NAME

class Database:
    def __init__(self,database):
        self.database = database

    def add_message_to_db(self,sender,message):
        current_timestamp = time.mktime(datetime.datetime.strptime(str(datetime.datetime.today()).split(" ")[0],'%Y-%m-%d').timetuple())
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO messages(sender_id,message,timestamp) VALUES((SELECT uid FROM userdata WHERE username=?),?,?)", [sender,message,current_timestamp])
        print(f"message from {sender} recieved")
        con.commit()
        con.close()

    def log_ip(self,request,username):
        request.environ['REMOTE_ADDR']
        con = sqlite3.connect(self.database)

    def create_user(self,username,password):
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("INSERT INTO userdata(username,password,ip,last_active) VALUES (?,?,?,?)", [username,password,0,0])
        con.commit()
        con.close()

        


#create_user("larry","betterpassword123")

db = Database(get_db_name())

#db.add_message_to_db("bob", "Hello larry!")