from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = "Sh1Y5VnPA"

# setuo the connection to the main databse Compustore
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MYSQL_DB']='CompuStore'
mysql_main =MySQL(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

UPLOAD_FOLDER='./app/static/uploads'

app.config.from_object(__name__)

# using a config value
filefolder=app.config['UPLOAD_FOLDER']

# setup the frontend
from app import views


