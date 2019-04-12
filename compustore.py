import requests
import random
import string

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def insertCusAcc(times):
    try:
        connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
        cursor = connection.cursor(prepared=True)
        
        s = set()
        for _ in range(0,times):
            sql_insert_data_query="INSERT INTO Laptop() VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
           
            result = cursor.execute( sql_insert_data_query, insert_tuple)
           
       connection.commit() 
       print ("Date Record inserted successfully into python_users table")
    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed") 



    compuStore = "USE CompuStore; \n\n INSERT INTO Laptop VALUES "
    branch1 = "\nUSE Branch1; \n\n INSERT INTO Laptop VALUES "
    branch2 = "\nUSE Branch2; \n\n INSERT INTO Laptop VALUES "
    branch3 = "\nUSE Branch3; \n\n INSERT INTO Laptop VALUES "
    

    ##noteb.com provides an api to get free limited access to its laptop database to anyone willing to develop or enhanced third party applications or websites.
    laptopModels = requests.post('https://noteb.com/api/webservice.php', data={"apikey": "112233aabbcc", "method": "list_models", "param[model_name]": ""})
    
    laptopModels = laptopModels.json()
    n = int(laptopModels["daily_hits_left"])

    k = 0
    for i in range(0,n):
        try:
            model = laptopModels["result"][str(i)]["model_info"][0]["name"]
        
            laptopInfo = requests.post('https://noteb.com/api/webservice.php', data={"apikey": "112233aabbcc", "method": "get_model_info", "param[model_name]": model})
            laptopInfo = laptopInfo.json()
            
            serialNum = "\"" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + "\""
            while serialNum in s:
                serialNum = "\"" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + "\""
            s.add(serialNum)

            model = "\"" + model + "\""
            
            brand = "\"" + model.split(" ")[0] + "\"" 

            launchDate = laptopInfo["result"]["0"]["model_resources"]["launch_date"] 
            cpu = laptopInfo["result"]["0"]["cpu"]["prod"] + " " + laptopInfo["result"]["0"]["cpu"]["model"]
            display = laptopInfo["result"]["0"]["display"]["size"] + "\"\"," + laptopInfo["result"]["0"]["display"]["horizontal_resolution"] + " x " + laptopInfo["result"]["0"]["display"]["vertical_resolution"] + " display"
            os = laptopInfo["result"]["0"]["operating_system"]
            gpu = laptopInfo["result"]["0"]["gpu"]["prod"] + " " + laptopInfo["result"]["0"]["gpu"]["model"]
            
            description = "\"CPU: %s\nDisplay: %s\nOperating System: %s\nGPU: %s\nLaunch Date: %s\"" % (cpu, display, os, gpu, launchDate)
                    
            thumbnail = "\"" + laptopInfo["result"]["0"]["model_resources"]["thumbnail"] + "\""

            price = "\"" + laptopInfo["result"]["0"]["config_price_max"] + "\""

            # CompuStore Laptop(serial_num, model, brand, description, thumbnail, price)
            # branch Laptop(serial_num, model, brand, description, picture, price)

            compuStore += "(%s, %s, %s, %s, %s, %s), " % (serialNum, model, brand, description, thumbnail, price)
            branch1 += "(%s, %s, %s, %s, %s), " % (serialNum, model, brand, description, thumbnail)
            branch2 += "(%s, %s, %s, %s, %s), " % (serialNum, model, brand, description, thumbnail)
            branch3 += "(%s, %s, %s, %s, %s), " % (serialNum, model, brand, description, thumbnail)
            print("writen model info to variable ... ")
            k+=1
        except Exception as e:
            continue

    
    compuStore = compuStore[:-2] + ";"
    branch1 = branch1[:-2] + ";"
    branch2 = branch2[:-2] + ";"
    branch3 = branch3[:-2] + ";"
   
