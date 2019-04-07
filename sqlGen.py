import mysql.connector

#attributes needed for the specification of columns in a table 
columns = {
    "creditCard": ("(", "acc_id,", "card_num",")"),
    "customer": ("(", "cus_id," ,"fname,","lname,", "age,","gender,", "date_of_birth,", "street,", "parish,", "telephone", ")"),
    "customerAccount": ("(", "acc_id,", "cus_id", ")"),
    "account": ("(", "acc_id,", "email,", "password,", "created_on", ")" ),
    "creditCardDetails":("(","card_num,", "expiration_date,", "cvc,", "street,", "city,", "parish",")"),
    "branch":("(","br_id,", "name,","street,", "city,", "parish,", "telephone",")"),
    "laptop":("(","serial_num,", "model,", "brand,", "description,", "image",")"),
    "purchase":("(","acc_id,","br_id,", "serial_num,", "date_made,", "quantity,", "cost", ")"),
    "cus_cart":("(","scart_id,", "name", ")"),
    "addTo":("(","scart_id,", "acc_id,", "br_id,", "serial_num,", "date_made", ")"),
    "transaction":("(","scart_id,", "track_num,", "total_cost,", "date_made",")"),
    "receipt":("(","track_num,", "invoice", ")"),
    "review":("(","rev_id,","rev_text",")"),
    "writeReview":("(","rev_id,","acc_id,", "serial_num,", "date_written", ")"),
    "warehouse":("(","wh_id,", "street,", "city,", "parish,", "telephone", ")"),
    "stores":("(","wh_id,","serial_num,", "quanitity", ")"),
    "sells":("(","serial_num,", "price,", "quantity", ")")
     
}


class databaseGenerator:
    def __init__(self, dbname, columns):
        self.dbname   = dbname
        self.column   = columns
        self.mydb     = mysql.connector.connect(host="localhost", user="root", passwd="", database=dbname)
        self.mycursor = self.mydb.cursor()

    # attrib is a list of the arributes for the record, 
    # table is the string with the name of the table 
    #NB: if the datatype in the db is varchar the arrib
    #value in the list should be represented as a quoted string
    def addRecord(self, attrib, name):
        try:
            strstatement  =""
            strstatement  ="INSERT INTO "+str(name)+" "+ "".join(self.column[name])
            strstatement += ' VALUES({});'.format(','.join("{0}".format(x) for x in attrib))
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for addRecord")

    #key is the identifier of the value to be removed
    #name is the name of the table to removed the record form
    #coltocompare is the name of the column to compare primkey against
    #NB: primkey must be a quoted string if datatype is varchar 
    def removeRecord(self, key, name, coltocompare):
        try:
            strstatement  = ""
            strstatement  = "DELETE FROM "+str(name)
            strstatement += " WHERE {} = {};".format(coltocompare, key)
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for removeRecord")

    #name of table must be python string
    def showTableAll(self, tableName):
        try:
            strstatement = ""
            strstatement = "SELECT * FROM {};".format(tableName)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input for showTableAll")

    #key must be quoted string if the datatype in the database is varchar or date
    #tableName - the name of the table to be updated
    # columntoupdate - name of column to be updated
    # selection - is the column to be selected
    #key - the unique identifier of the record
    #NT
    def showTableCondition(self, tableName, coltocompare, key, selection):
        try:
            strstatement = ""
            strstatement = "SELECT {} FROM {} WHERE {} = {};".format(selection, tableName, coltocompare, key)
            self.mycursor.execute(strstatement)
            records = self.mycursor.fetchall()
            return records
        except:
            print("Please check input for showTableCondition")
        
    #key must be quoted string if the datatype in the database is varchar or date
    #tableName - the name of the table to be updated
    # columntoupdate - name of column to be updated
    # value - is the new value of the column
    #key - the unique identifier of the record
    #idfn - the column to compare to key in order to find specified record
    def updateRecord(self, tableName, columntoupdate, key, value, idfn ):
        try:
            strstatement = ""
            strstatement = "UPDATE {} SET {} = {} WHERE {} = {};".format(tableName, columntoupdate, value, idfn, key )
            self.mycursor.execute(strstatement)
        except:
            print("Pease check input for updateRecord")


    #tableName - the name of the table to be updated
    # column - name of column to be updated
    # value - is the new value of the column 
    def updateTable(self, tableName, column, value):
        try:
            strstatement = ""
            strstatement = "UPDATE {} SET {} = {};".format(tableName, column, value)
            self.mycursor.execute(strstatement)
        except:
            print("Please check input for updateTable")

    #destructor closes database and connection
    def __del__(self): 
        self.mycursor.close()
        self.mydb.close()


if __name__ == "__main__":
    db = None
    db = databaseGenerator("compustore", columns)
    
    #testing code
    #tb = db.showTableCondition("test", "Username", "\"popii\"", "Password")
    #print(tb)
    #t  = db.showTableAll("test")
    #print(t)
    #db.updateRecord("managers", "person_name", "\"john\"","\"Grim\"", "person_name") 
    #db.updateTable("test", "id", "1234*2")

    #db.addRecord(["\"1234\"", "\"hviujk\"", "\"gdfku\"","\"hjfgf\""], "test")
    #db.addRecord(["\"john\"", "\"samuels\""], "managers")
    #n.addRecord([7564, 657437,], "creditcard")
    #db.removeRecord("\"Luke\"", "managers", "manager_name")

