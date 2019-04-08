from app import app, mysql 
from flask import render_template, request, redirect, url_for, flash

@app.route("/", methods=['GET', 'POST'] )
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT firstName, lastName FROM test.MyUsers")
    rv = cur.fetchall()
    
    return render_template("home.html",data=rv[0][0],datas=rv[0][1])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
