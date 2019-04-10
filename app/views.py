from app import app, mysql 
from flask import render_template, request, redirect, url_for, flash
from forms import LoginForm, SignupForm

@app.route("/", methods=['GET', 'POST'] )
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT firstName, lastName FROM test.MyUsers")
    rv = cur.fetchall()
    
    return render_template("home.html",data=rv[0][0],datas=rv[0][1])
    
    
@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Login and validate the user.
    #if request.method == 'POST' and form.validate_on_submit():
    return render_template("login.html",form=form)

@app.route("/sign-up")
def signup():
       form = SignupForm()
       return render_template("signup.html",form=form)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
       
       
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
