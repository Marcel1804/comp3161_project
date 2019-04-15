from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('ConfirmPassword', validators=[DataRequired()])

class UploadForm(FlaskForm):
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',"file allowed"])])
    description = StringField('Description', validators=[DataRequired()])

class Creditcard(FlaskForm):
    cardNum =StringField('Card Number', validators=[DataRequired()])
    name_on_card =StringField('Name_on_card', validators=[DataRequired()])
    card_security_code =StringField('Card_security_code', validators=[DataRequired()])
    expiration_month =StringField('Expiration_month', validators=[DataRequired()])
    expiration_year =StringField('Expiration_year', validators=[DataRequired()])
    billing_street =StringField('Billing_street', validators=[DataRequired()])
    billing_city =StringField('Billing_city', validators=[DataRequired()])
    billing_parish =StringField('Billing_parish', validators=[DataRequired()])


    