from faker import Faker
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
import sqlGen
from recordGenerator import getGender
fake=Faker()

# use to populate the CustomerAccount table in the CompuStoreDB
gender=['Male','Female']
parish = ['Portland','St Mary','St Thomas','St Ann','Kingston','St Andrew','St Catherine','St Jame','Manchester','Hanover','Clarendon','Westmoreland','Trelawny','St Elizabeth']
#CustomerAccount(acc_id, email, password,  fname, lname, gender, date_of_birth, street, city, parish, telephone, created_on)
def insertCusAcc(times):
    try:
       connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
       cursor = connection.cursor(prepared=True)
        
       for _ in range(0,times):
           gen=gender[random.randint(0,1)]
           sql_insert_data_query="INSERT INTO CustomerAccount(email,password,fname,lname,gender,date_of_birth,street,city,parish,telephone,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

           if gen=='Male':
               insert_tuple=(fake.email(), fake.password(),fake.first_name_male(),fake.last_name(),gen,fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=85),fake.street_address(),fake.city(),parish[random.randint(0,13)],fake.phone_number(),fake.date(pattern="%Y-%m-%d", end_datetime=None))

           else:
               insert_tuple=(fake.email(), fake.password(),fake.first_name_female(),fake.last_name(),gen,fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=85),fake.street_address(),fake.city(),parish[random.randint(0,13)],fake.phone_number(),fake.date(pattern="%Y-%m-%d", end_datetime=None))

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

## use to populate the CreditCardDetails table and CustomerCeditCard in the CompuStoreDB
#CreditCardDetails(card_num, expiration_month, expiration_year, billing_street, billing_city, billing_parish)
#CustomerCreditCard(acc_id, card_num)
def insertCard(times):
     try:
       connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
       cursor = connection.cursor(prepared=True)
        
       for _ in range(0,times):
           sql_insert_data_query="INSERT INTO CreditCardDetails(card_num, expiration_month, expiration_year, billing_street, billing_city, billing_parish) VALUES (%s,%s,%s,%s,%s,%s,%s)"

           insert_tuple=()
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
    

# Branch(br_id, name, street, city, thumbnail, telephone)
# Laptop(serial_num, model, brand, description, picture, price)

# CustomerCart(acc_id, item_count, value)

# CartItems(acc_id, serial_num, br_id, quantity, cost, purchasing, date_added)

# Receipt(track_num, invoice)
# Checkout(acc_id, track_num, total_cost, transaction_date)

# PurchasedItem(pur_id, acc_id, serial_num, br_id, quantity, cost, date_purchased)

# WriteReview(acc_id, serial_num, rev_text, date_written)

# Warehouse(wh_id, street, city, parish, telephone)
# Stores(wh_id, serial_num, quantity)

# def generateTest():
#     n = sqlGen.databaseGenerator("CompustoreDB", sqlGen.columns)
#     n.addRecords([fake.email(), fake.password(), fake.first_name_male(), fake.last_name(), getGender(), fake.date_of_birth()], "CustomerAccount")
    
     