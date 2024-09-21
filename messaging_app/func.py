import sqlite3
import yaml

def get_db_name():
    with open("config.yaml") as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        DB_NAME = conf["database_name"]
        return DB_NAME


def create_user(username,password):
    con = sqlite3.connect(get_db_name())
    cursor = con.cursor()
    cursor.execute("INSERT INTO userdata(username,password,ip,last_active) VALUES (?,?,?,?)", [username,password,0,0])
    cursor.execute("INSERT INTO messages() VALUES (?,?,?,?)", []) # DO AN INSERT INTO MESSAGES TABLE TOO PLEASE
    con.commit()
    con.close()

create_user("bob","password123")