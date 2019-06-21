from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = "Sh1Y5VnPA"

# setuo the connection to the main databse Compustore
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MYSQL_DB']='CompuStore'
mysql_main =MySQL(app)

# setup the frontend
from app import views


