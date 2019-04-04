import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"

SQLALCHEMY_DATABASE_URI = 'mysql://niikou:@localhost/compustore'

SQLALCHEMY_BINDS = {
    'branch1': 'mysql://niikou:@localhost/branch1.db',
    'branch2': 'mysql://niikou:@localhost/branch2.db',
    'branch3': 'mysql://niikou:@localhost/branch3.db'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
