from faker import Faker
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
import sqlController
from  insertLaptops import recordGenerator 
import getGender
fake=Faker()


def phoneNumber():
    p=list('(876)-000-0000')
    p[6] = str(random.randint(1,9))
    for i in [7,8,10,11,12,13]:
        p[i] = str(random.randint(0,9))
        
    p = ''.join(p)
    return p[:5]+ ''+ p[5:9] +''+ p[9:]
    
def year():
    p=list('2000')
    p[2] = str(random.randint(2,3))
    p[3] = str(random.randint(0,9))
    p = ''.join(p)
    return p[:2]+''+ p[2:]
    
def cardNum():
    p=list('0000000000000000')
    p[0] = str(random.randint(1,9))
    for i in range(1,16):
         p[i] = str(random.randint(0,9))
    p = ''.join(p)
    return p[:1]+''+ p[1:]
    
def cardSC():
    p=list('000')
    for i in range(0,3):
         p[i] = str(random.randint(0,9))
    p = ''.join(p)
    return int(p[0:])
    
# use to populate the CustomerAccount table in the CompuStoreDB 
gender=['Male','Female']
parish = ['Portland','St Mary','St Thomas','St Ann','Kingston','St Andrew','St Catherine','St Jame','Manchester','Hanover','Clarendon','Westmoreland','Trelawny','St Elizabeth']
#CustomerAccount(acc_id, email, password, fname, lname, gender, date_of_birth, street, city, parish, telephone, created_on)
def insertCusAcc(times):
    try:
       connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
       cursor = connection.cursor(prepared=True)
        
       for _ in range(0,times):
           gen=gender[random.randint(0,1)]
           sql_insert_data_query="INSERT INTO CustomerAccount(email,password,fname,lname,gender,date_of_birth,street,city,parish,telephone,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

           if gen=='Male':
               insert_tuple=(fake.email(), fake.password(),fake.first_name_male(),fake.last_name(),gen,fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=50),fake.street_address(),fake.city(),parish[random.randint(0,13)],phoneNumber(),fake.date_between(start_date="-10y", end_date="today"))

           else:
               insert_tuple=(fake.email(), fake.password(),fake.first_name_female(),fake.last_name(),gen,fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=50),fake.street_address(),fake.city(),parish[random.randint(0,13)],phoneNumber(),fake.date_between(start_date="-10y", end_date="today") )

           cursor.execute( sql_insert_data_query, insert_tuple)
           
       connection.commit() 
       print ("Date Record inserted successfully into CustomerAccount table")
    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed") 

## use to populate the CreditCardDetails table and CustomerCeditCard in the CompuStoreDB
#CreditCardDetails(card_num,name_on_card, card_security_code,expiration_month, expiration_year, billing_street, billing_city, billing_parish)
#CustomerCreditCard(acc_id, card_num)
def insertCard(start,end):
    try:
        connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
        cursor = connection.cursor(prepared=True)
        for i in range(start,end):
            # fetching information about customer from CustomerAccount table 
            cursor.execute("SELECT acc_id, fname, lname, street, city, parish FROM CompuStore.CustomerAccount where acc_id={}".format(i))
            result = cursor.fetchone()
            name=result[1].decode()+" "+result[2].decode()
            
            # insert data into the CreditCardDetail table
            card=cardNum()
            sql_insert_data_query="INSERT INTO CreditCardDetails(card_num,name_on_card,card_security_code,expiration_month,expiration_year,billing_street,billing_city,billing_parish) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            insert_tuple=(card,name,cardSC(),fake.month(),year(),result[3].decode(),result[4].decode(),result[5].decode())
            cursor.execute( sql_insert_data_query,insert_tuple)
            
            # insert data into the CustomerCreditCard table
            sql_insert_data_query="INSERT INTO CustomerCreditCard(acc_id,card_num) VALUES (%s,%s)"
            insert_tuple=(result[0],card)
            cursor.execute( sql_insert_data_query,insert_tuple)
            
            
        connection.commit() 
        print ("Date Record inserted successfully into tables")
    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
    

# Branch(br_id, name, street, city, thumbnail, telephone)
def insertBranch(num):
    parish = []
    for i in range(num):
        now = datetime.datetime.now() 
        brid = "'"+str(int(now.second))+str(int(now.microsecond))+"'"
        name = "\"KingstonBranch\""
        fake  = Faker()
        fake = fake.address()
        street = fake.split(',')[0]
    
    conn = sqlController.databaseGenerator("CompuStore")
    conn.addRecord([brid, name, street, ], "Branch")



# Laptop(serial_num, model, brand, description, picture, price)

# CustomerCart(acc_id, item_count, value)

# CartItems(acc_id, serial_num, br_id, quantity, cost, purchasing, date_added)


# Warehouse(wh_id, street, city, parish, telephone)
def insertWarehouse(times):
    try:
        for _ in range(0,times):
            connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
            cursor = connection.cursor(prepared=True)
            sql_insert_data_query="INSERT INTO Warehouse(street,city,parish,telephone) VALUES (%s,%s,%s,%s)"
            insert_tuple=(fake.street_address(),fake.city(),parish[random.randint(0,13)],phoneNumber())
            cursor.execute( sql_insert_data_query, insert_tuple)
            
        connection.commit() 
        print ("Date Record inserted successfully into Warehouse table")
    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed") 

# WarehouseStock(wh_id, model_id, quantity) need editing
def insertWaresStock(start,end):
    try:
        for _ in range(0,times):
            connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStore")
            cursor = connection.cursor(prepared=True)
            sql_insert_data_query="INSERT INTO Warehouse(model_id,quantity) VALUES (%s,%s)"
            insert_tuple=()
            cursor.execute( sql_insert_data_query, insert_tuple)
            
        connection.commit() 
        print ("Date Record inserted successfully into WareStock table")
    except mysql.connector.Error as error :
        print("Failed inserting date object into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed") 
    
# Receipt(track_num, invoice)

# Checkout(acc_id, track_num, total_cost, transaction_date)

# PurchasedItem(pur_id, acc_id, serial_num, br_id, quantity, cost, date_purchased)

# WriteReview(acc_id, serial_num, rev_text, date_written)
# ModelStockInfo(model_id, amt_in_stock, amt_sold) */
# ModelItems(product_id, model_id) */
# CreditCardDetails(card_num, name_on_card, card_security_code, expiration_month, expiration_year, billing_street, billing_city, billing_parish) */
