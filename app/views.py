from app import app, mysql 
from flask import render_template, request, redirect, url_for, flash

@app.route("/", methods=['GET', 'POST'] )
def home():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
