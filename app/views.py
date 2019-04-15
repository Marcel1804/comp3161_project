from app import app, mysql # use to connect to the main databases CompuStore
from flask import render_template, request, redirect, url_for, flash
from forms import LoginForm, SignupForm, Creditcard 

# use to connected to the other database
#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import errorcode


@app.route("/", methods=['GET', 'POST'] )
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM CompuStore.CustomerAccount where acc_id=1")
    rv = cur.fetchone()#.all()
    
    return render_template("home.html",data=rv)
    
    
@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Login and validate the user.
    #if request.method == 'POST' and form.validate_on_submit():
    return render_template("login.html",form=form)

@app.route("/sign-up",methods=['GET', 'POST'])
def signup():
       form = SignupForm()
       return render_template("signup.html",form=form)

@app.route("/admin")
def admin():
       return render_template("admin.html")

@app.route("/about")
def about():
       return render_template("about.html")

@app.route("/cart")
def cart():
       return render_template("cart.html")

@app.route("/checkout")
def checkout():
       return render_template("checkout.html")

@app.route("/creditCart",methods=['GET', 'POST'])
def creditCart():
       form =Creditcard()
       return render_template("creditCart.html",form=form)
       
@app.route("/laptop")
def laptop():
       return render_template("laptop.html")

@app.route("/profile_page")
def profile_page():
       return render_template("profile_page.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/secure_page")
def secure_page():
       return render_template("secure_page.html")
       
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
