'''import json
file = open("cretentials.json")
x = json.load(file)
print(x)
#print(x["db_password"])'''

import mysql.connector

def db_connect():
    mydb = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password = "studies123",
        database = 'registry'
    )
    return(mydb.cursor())

name ="sdfgg"
phone = 79856
db_connect()
sql = "INSERT INTO client_registry VALUES (last_insert_id(), %s, %s)"
value = (name, phone)
dbconnect().execute(sql,value)
#mydb.commit()