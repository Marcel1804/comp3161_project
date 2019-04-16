from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, ValidationError
from wtforms.validators import DataRequired,EqualTo,Email,Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email("Please enter your email address.")])
    gender = SelectField('Gender', choices=[('Male','Male'), ('Female', 'Female')])
    date_of_birth = StringField('D.O.B', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    parish = StringField('Parish', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6,max=100,message="must be aleast 6 characters or more"),EqualTo('confirmpassword', message='Passwords must match')])
    confirmpassword = PasswordField('ConfirmPassword', validators=[DataRequired()])

class UploadForm(FlaskForm):
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',"file allowed"])])
    description = StringField('Description', validators=[DataRequired()])
    # detail=TextAreaField('detail', validators=[DataRequired()])

class Creditcard(FlaskForm):
    cardNum =StringField('Card Number', validators=[DataRequired()])
    name_on_card =StringField('Name_on_card', validators=[DataRequired()])
    card_security_code =StringField('Card_security_code', validators=[DataRequired()])
    expiration_month =StringField('Expiration_month', validators=[DataRequired()])
    expiration_year =StringField('Expiration_year', validators=[DataRequired()])
    billing_street =StringField('Billing_street', validators=[DataRequired()])
    billing_city =StringField('Billing_city', validators=[DataRequired()])
    billing_parish =StringField('Billing_parish', validators=[DataRequired()])

class Search(FlaskForm):
    search =StringField('search', validators=[DataRequired()])

#Custom validators
# class MyForm(Form):
#     name = StringField('Name', [InputRequired()])

#     def validate_name(form, field):
#         if len(field.data) > 50:
#             raise ValidationError('Name must be less than 50 characters') 

    