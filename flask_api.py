from flask import Flask, jsonify, request
import mysql.connector
import json

app = Flask(__name__)

@app.route("/")
def home():
    return ("Hello")

# loading the file with db cretentials and app admin cretentials.
# it is always better to keep the cretential files out of python code.
file = open("cretentials.json")
cretentials = json.load(file)

mydb = mysql.connector.connect(
    host = cretentials["db_host"],
    user =cretentials["db_user"],
    password = cretentials['db_password'],
    database = cretentials['db_name']
)
cursor = mydb.cursor()


@app.route("/register", methods = ['POST'])
def applicant():
    data = request.get_json()
    name = data['name']
    phone = data['phone']
    
    sql = "INSERT INTO client_registry VALUES (last_insert_id(), %s, %s)"
    value = (name, phone)
    cursor.execute(sql,value)
    mydb.commit()
              
    return({"Message":"Registered"})

@app.route("/admin", methods = ["POST"])
def admin():
    data = request.get_json()
    password = cretentials['admin_password']

    if data['password'] == password:

       given_data = []
       for i in data:
            given_data.append(i)

       if "name" in given_data:
            name = data["name"]
            sql = "SELECT * FROM client_registry WHERE `name` = "+"'" + str(name)+ "'"
            cursor.execute(sql)
            results =cursor.fetchall()
            
            for x in results:
                message = x
               
            return({"message" : message})
       
       elif "value" in given_data:
            if data["value"] == "all":
                sql = "SELECT * FROM client_registry"
                cursor.execute(sql)
                results =cursor.fetchall()
                message = []
                for x in results:
                    message.append(x)
            return jsonify({"message" : message})
       
       elif "phone" in given_data:
            phone = data["phone"]
            sql = "SELECT * FROM client_registry WHERE `phone` = "+"'" + str(phone)+ "'"
            cursor.execute(sql)
            results =cursor.fetchall()
            message = []
            for x in results:
                message.append(x)
            return jsonify({"message" : message})
       
       elif 'reg_no' in given_data:
            reg_no = data["reg_no"]
            sql = "SELECT * FROM client_registry WHERE `reg_no` = "+"'" + reg_no + "'"
            cursor.execute(sql)
            results =cursor.fetchall()
            for x in results:
                message = x
            return jsonify({"message" : message})
       else:
            return(jsonify({"message" : "Invalid input or not registered"}))

    return()

if __name__ =="__main__":
        app.run(debug=True)
 
    