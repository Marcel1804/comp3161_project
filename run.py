#! /usr/bin/env python
import os

os.system('sudo service mysql start')
from app import app
app.run(debug=True,host="0.0.0.0",port=8080)