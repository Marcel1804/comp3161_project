from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MYSQL_DB']='CompuStore'

mysql =MySQL(app)


from app import views


