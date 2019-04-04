from . import db
import datetime
from sqlalchemy import DateTime
from werkzeug.security import generate_password_hash

class customer(db.Model):
   # __bind_key__ = 'compustore'
    __tablename__ = 'customer'

    cus_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(10), nullable=False)
    #updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    
 
    def __repr__(self):
        return "<{}:{} {}>".format(self.id, self.fname, self.lname)

    
    def __init__(self, fname, lname, street, city, parish, telephone):
        """"""
        self.fname = fname
        self.lname = lname
        self.street = street
        self.city = city
        self.parish = parish
        self.telephone = telephone

    def get_id(self):
            try:
                return unicode(self.id)  # python 2 support
            except NameError:
                return str(self.id)  # python 3 support

class customerAccount(db.Model):
    __tablename__ = 'customerAccount'

    acc_id = db.Column(db.Integer, primary_key=True)
    cus_id = db.Column(db.Integer, primary_key=True)

class account(db.Model):
    __tablename__ = 'account'

    acc_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(DateTime, default=datetime.datetime.now().strftime("%B %d, %Y") )

    def __init__(self, username, email, password):
        """"""
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

class creditCard(db.Model):
    __tablename__ = 'creditCard'

    acc_id = db.Column(db.Integer, primary_key=True)
    card_num = db.Column(db.Integer, primary_key=True)

class creditCardDetails(db.Model):
    __tablename__ = 'creditCardDetails'

    card_num = db.Column(db.Integer, primary_key=True)
    cvc = db.Column(db.String(30), nullable=False, unique=True)
    expiration_date = db.Column(DateTime)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    
    def __init__(self, card_num, cvc, expiration_date, street, city, parish):
        """"""
        self.card_num = card_num
        self.cvc = cvc
        self.expiration_date = expiration_date
        self.street = street
        self.city = city
        self.parish = parish
        
class branch(db.Model):
    __tablename__ = 'branch'

    br_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(50), nullable=False)
    
    def __init__(self, name, street, city, parish, telephone):
        """"""
        self.name = name
        self.telephone = telephone
        self.street = street
        self.city = city
        self.parish = parish

class laptop(db.Model):
    __tablename__ = 'laptop'

    serial_num = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(30), nullable=False, unique=True)
    brand = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(50), nullable=False)
    
    def __init__(self, serial_num, model, brand, description, image):
        """"""
        self.serial_num = serial_num
        self.model = model
        self.brand = brand
        self.description = description
        self.image = image


class purchase(db.Model):
    __tablename__ = 'purchase'

    acc_id = db.Column(db.Integer, primary_key=True)
    br_id = db.Column(db.String(30), nullable=False, unique=True)
    serial_num = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date_purchased = db.Column(DateTime, default=datetime.datetime.now().strftime("%B %d, %Y") )

    def __init__(self, acc_id, br_id, serial_num, quantity, cost):
        """"""
        self.acc_id = acc_id
        self.br_id = br_id
        self.serial_num = serial_num
        self.quantity = quantity
        self.cost = cost

class cus_cart(db.Model):
    __tablename__ = 'cus_cart'

    cart_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    def __init__(self, name):
        """"""
        self.name = name

class addToCart(db.Model):
    __tablename__ = 'addToCart'

    cart_id = db.Column(db.Integer, primary_key=True)
    acc_id = db.Column(db.Integer, primary_key=True)
    br_id = db.Column(db.Integer, primary_key=True)
    serial_num = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(DateTime, default=datetime.datetime.now().strftime("%B %d, %Y") )

    def __init__(self, cart_id, acc_id, br_id, serial_num):
        """"""
        self.cart_id = cart_id
        self.acc_id = acc_id
        self.br_id = br_id
        self.serial_num = serial_num

class transaction(db.Model):
    __tablename__ = 'transaction'

    cart_id = db.Column(db.Integer, primary_key=True)
    track_num = db.Column(db.Integer, primary_key=True)
    total_cost = db.Column(db.Integer, nullable=False)
    date_made = db.Column(DateTime, default=datetime.datetime.now().strftime("%B %d, %Y") )

    def __init__(self, cart_id, track_num, total_cost):
        """"""
        self.cart_id = cart_id
        self.track_num = track_num
        self.total_cost = total_cost  

class receipt(db.Model):
    __tablename__ = 'receipt'

    track_num = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(30), nullable=False, unique=True)
    
    def __init__(self, invoice):
        """"""
        self.invoice = invoice

class review(db.Model):
    __tablename__ = 'review'

    rev_id = db.Column(db.Integer, primary_key=True)
    rev_text = db.Column(db.Text(), nullable=False)
    
    def __init__(self, rev_text):
        """"""
        self.rev_text = rev_text

class writeReview(db.Model):
    __tablename__ = 'writeReview'

    rev_id = db.Column(db.Integer, primary_key=True)
    acc_id = db.Column(db.Integer, primary_key=True)
    serial_num = db.Column(db.Integer, nullable=False)
    date_written = db.Column(DateTime, default=datetime.datetime.now().strftime("%B %d, %Y") )

    def __init__(self, rev_id, acc_id, serial_num):
        """"""
        self.rev_id = rev_id
        self.acc_id = acc_id
        self.serial_num = serial_num  

class warehouse(db.Model):
    __tablename__ = 'warehouse'

    wh_id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    parish = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(50), nullable=False)
    
    def __init__(self, street, city, parish, telephone):
        """"""
        self.telephone = telephone
        self.street = street
        self.city = city
        self.parish = parish

class stores(db.Model):
    __tablename__ = 'stores'

    wh_id = db.Column(db.Integer, primary_key=True)
    serial_num = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, wh_id, serial_num, quantity):
        """"""
        self.wh_id = wh_id
        self.serial_num = serial_num
        self.quantity = quantity  

class sells1(db.Model):
    __bind_key__ = 'branch1'

    __tablename__ = 'sells'

    serial_num = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, serial_num, price, quantity):
        """"""
        self.serial_num = serial
        self.price = price
        self.quantity = quantity

class sells2(db.Model):
    __bind_key__ = 'branch2'

    __tablename__ = 'sells'

    serial_num = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, serial_num, price, quantity):
        """"""
        self.serial_num = serial
        self.price = price
        self.quantity = quantity

class sells3(db.Model):
    __bind_key__ = 'branch3'

    __tablename__ = 'sells'

    serial_num = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, serial_num, price, quantity):
        """"""
        self.serial_num = serial
        self.price = price
        self.quantity = quantity
