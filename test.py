from faker import Faker
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
fake=Faker()


parish = ['Portland','St Mary','St Thomas','St Ann','Kingston','St Andrew','St Catherine','St Jame','Manchester','Hanover','Clarendon','Westmoreland','Trelawny','St Elizabeth']



#CustomerAccount(acc_id, email, password,  fname, lname, gender, date_of_birth, street, city, parish, telephone, created_on)
def insertCusAcc(times):
    try:
       connection= mysql.connector.connect(host="localhost", user="root", password="", database="CompuStoreDB")
       cursor = connection.cursor(prepared=True)
       for _ in range(0,times):
           sql_insert_data_query="INSERT INTO CustomerAccount(email,password,fname,lname,gender,date_of_birth,street,city,parish,telephone,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           insert_tuple=(fake.email(), fake.password(),fake.first_name_male(),fake.last_name(),'Male',fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=85),fake.street_address(),fake.city(),parish[random.randint(0,5)],fake.phone_number(),fake.date(pattern="%Y-%m-%d", end_datetime=None))
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

        
#f= open("testresult.txt","w+")
#f.write()
#f.close()
# cur = mysql.connection.cursor()
# conncection = MYSQL.connect("name.db")
# cursor =connection.cusror()
# cursor.execute("create table")
# cursor.execute("insert into table values :name, :address, :email",{'name':fake_data.name(),'address':fake_data.address(),'email':fake_data.email()})

# cursor.execute('selesct * from tables')

# for i in cursor.excute('select name, address, email from table'):
#     print(i)

# connection.commit()
# connection.close()

