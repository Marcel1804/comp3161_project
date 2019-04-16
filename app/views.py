from app import app, mysql_main,login_manager  # use to connect to the main databases CompuStore
from flask import render_template, request, redirect, url_for, url_for, flash, session, abort
from forms import LoginForm, SignupForm, Creditcard, Search, UploadForm
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required
import os
import datetime
from werkzeug.utils import secure_filename

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# connection to the databases

branch1Connection = mysql.connector.connect(host="localhost", user="root", password="", database="Branch1")
branch1Cursor = branch1Connection.cursor(prepared=True)

branch2Connection = mysql.connector.connect(host="localhost", user="root", password="", database="Branch2")
branch2Cursor = branch2Connection.cursor(prepared=True)

branch3Connection = mysql.connector.connect(host="localhost", user="root", password="", database="Branch3")
branch3Cursor = branch3Connection.cursor(prepared=True)

MultiLinkConnection = mysql.connector.connect(host="localhost", user="root", password="", database="MultiLink")
MultiLinkCursor = MultiLinkConnection.cursor(prepared=True)

@app.route("/", methods=['GET', 'POST'] )
def home():
    form=Search()
    # it work but not needed here.
    #CompuStore = mysql_main.connection.cursor()
    #CompuStore.execute("call getByModel('Acer')")
    #rv = CompuStore.fetchall()
    return render_template("home.html",form=form)
    
    
@app.route("/login",methods=['GET', 'POST'])
@login_required
def login():
    form = LoginForm()
    # # Login and validate the user.
    # if current_user.is_authenticated:
    #     # if user is already logged in, just redirect them to our secure page
    #     # or some other page like a dashboard
    #      return redirect(url_for('secure_page'))

    # # Here we use a class of some kind to represent and validate our
    # # client-side form data. For example, WTForms is a library that will
    # # handle this for us, and we use a custom LoginForm to validate.
    # form = LoginForm()
    # # Login and validate the user.
    # if request.method == 'POST' and form.validate_on_submit():
    #     # Query our database to see if the username and password entered
    #     # match a user that is in the database.
    #     username = form.username.data
    #     password = form.password.data

    #     # user = UserProfile.query.filter_by(username=username, password=password)\
    #     # .first()
    #     # or
    #     user = UserProfile.query.filter_by(username=username).first()
        
    #     if user is not None and check_password_hash(user.password, password):
    #         remember_me = False
            
    #         if 'remember_me' in request.form and username!='admin' :
    #             remember_me = True
        
    #         # If the user is not blank, meaning if a user was actually found,
    #         # then login the user and create the user session.
    #         # user should be an instance of your `User` class
    #         login_user(user, remember=remember_me)
            
    #         if  username=='admin':
    #             flash('Logged in successfully.', 'success')
    #             login_user(user)
    #             return redirect(url_for('admin'))
    #         else:
    #             flash('Logged in successfully.', 'success')
    #             next_page = request.args.get('next')
    #             return render_template('profile_page.html',name=username)
    #     else:
    #         flash('Username or Password is incorrect.', 'danger')

    # flash_errors(form)
    return render_template("login.html",form=form)

@app.route("/sign-up",methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # """Render a secure page on our website that only logged in users can access."""
    if current_user.is_authenticated:
         # if user is already logged in, just redirect them to our secure page
        # or some other page like a dashboard
        return redirect(url_for('secure_page'))
        
    # Signup and validate the user.
    if request.method == 'POST' and form.validate_on_submit():
        # Query our database to see if the username and password entered
        # match a user that is in the database.
        username = form.username.data
        firstname = form.firstname.data
        lastname=form.lastname.data
        email= form.email.data
        gender= form.gender.data
        dof= form.date_of_birth.data
        street= form.street.data
        city = form.city.data
        parish= form.parish.data
        telephone= form.telephone.data
        password = form.password.data
        confirmpassword = form.confirmpassword.data
        created_on=datetime.datetime.now()
         
        print(username,firstname,lastname,email,gender,dof,street,city,parish,telephone,password,confirmpassword)
        CompuStore = mysql_main.connection.cursor()
        CompuStore.execute("select * from CustomerAccount where username = '{}'".format(username))
        user = CompuStore.fetchone()
        print(user)
        print(dof[1],len(dof))
        # if user is None :
        # sql_insert_data_query= "INSERT INTO CustomerAccount(username,email,password,fname,lname,gender,date_of_birth,street,city,parish,telephone,created_on) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".formate(username,email,generate_password_hash(password,"sha256"),firstname,lastname,gender,dof,street,city,parish,telephone,created_on)
        
        #         CompuStore.execute(sql_insert_data_query)
        #         CompuStore.commit() 
        #         flash('Sign-up was successfully.', 'success')

    #             next_page = request.args.get('next')
    #             login_user(user)
    #             return redirect(next_page or url_for('home'))
    #         else:
    #             flash("Password and Confirmpassword don't match", 'danger')
                
    #     elif user is not None:
    #          flash("already a member", 'danger')
    #          return redirect(url_for('login'))
             
    flash_errors(form)
    return render_template("signup.html",form=form)

@app.route("/admin")
#@login_required
def admin():
    photoform=UploadForm()
    # Validate file upload on submit
    if request.method == 'POST'and photoform.validate_on_submit():
        # Get file data and save to your uploads folder
        photo= photoform.photo.data #we can also use request.file['photo']
        description= photoform.description.data
        
        filename= secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File Saved', 'success')
        return render_template('admin.html',form=photoform)
    flash_errors(photoform)
    return render_template("admin.html")

@app.route("/about")
def about():
       return render_template("about.html")

@app.route("/cart")
#@login_required
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

@app.route("/accessories")
def accessories():
    return render_template("accessories.html")

@app.route("/profile_page")
#@login_required
def profile_page():
       return render_template("profile_page.html")


@app.route("/review")
#@login_required
def review():
    return render_template("review.html")
    

@app.route("/secure_page")
def secure_page():
       return render_template("secure_page.html")

@app.route("/logout")
#@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))

# @login_manager.user_loader
# def load_user(id):
#     return UserProfile.query.get(int(id))

# Flash errors frrom the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
      
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
