from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

'''
@app.route("/")
def home():
    return ("Hello")
'''

@app.route("/register", methods = ['POST'])
def applicant():
    data = request.get_json()
    name = data['name']
    phone = data['phone']
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user ="root",
        password = "studies123",
        database = 'registry'
    )
    cursor = mydb.cursor()

    sql = "INSERT INTO client_registry VALUES (last_insert_id(), %s, %s)"
    value = (name, phone)
    cursor.execute(sql,value)
    mydb.commit()
              
    return({"Message":"Registered"})

@app.route("/admin", methods = ["POST"])
def admin():
    data = request.get_json()
    password = "password"

    if data['password'] == password:
        
       mydb = mysql.connector.connect(
       host = "localhost",
       user ="root",
       password = "studies123",
       database = 'registry'
       )   
       cursor = mydb.cursor()

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
            
            for x in results:
                message = x
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
 
    