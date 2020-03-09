from config import *

#-- flask-sqlalchemy classes and methods
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#-- initiate database and connecti it to app
db = SQLAlchemy(app)

# For migration
# Migrate with app,db as super classes
migrate = Migrate(app,db)
"""
flask db init
flask db migrate -m "comment"
flask db upgrade
"""

############################# Security models
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with


############################# Customers

class Customer(db.Model):
    #-- Customer Table
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(80,), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False)
    basket = db.Column(db.String(40), nullable=True, default="None")
    buy = db.Column(db.String(40), nullable=True, default="None")

    #-- For debuging i use __str__
    # def __repr__(self):
    #     return "<Customer %r>" % self.customer_id, self.first_name, self.last_name, self.address, self.email, self.phone, self.basket, self.buy

    # This is a modified __repr__ method above. for some reason i customerouldnt have a correct out come in CLI test mode
    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.customer_id, self.first_name, self.last_name, self.address, self.email, self.phone, self.basket, self.buy)

#####################################  Customer Search functions
def search_customer_id(customer_id):
    customers = Customer.query.filter_by(customer_id=customer_id).all()
    if len(customers) == 0:
        return "404"
    return customers

def search_address(address):
    customers = Customer.query.filter_by(address=address).all()
    if len(customers) == 0:
        return "404"
    return customers

def search_firstname(first_name):
    customers = Customer.query.filter_by(first_name=first_name).all()
    if len(customers) == 0:
        return "404"
    return customers


def search_lastname(last_name):
    customers = Customer.query.filter_by(last_name=last_name).all()
    if len(customers) == 0:
        return "404"
    return customers

def search_email(email):
    customers = Customer.query.filter_by(email=email).all()
    if len(customers) == 0:
        return "404"
    return customers

def search_phone(phone):
    customers = Customer.query.filter_by(phone=phone).all()
    if len(customers) == 0:
        return "404"
    return customers


#####################################

#-- Returns all customers
def show_all_customers():
    all_customers = Customer.query.all()
    return all_customers

#-- Returns a single customer by ID
def get_customer(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    return customer

#-- Add new customer
#-- Inserting new record to table
def insert_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy):
        check_customer = Customer.query.filter_by(customer_id=customer_id).first()
        if check_customer is None:
            new_customer =  Customer(customer_id = customer_id, first_name=first_name, last_name=last_name, address=address, email=email, phone=phone, basket=basket, buy=buy)
            db.session.add(new_customer)
            db.session.commit()
            return True
        else:
            return False
#-- Delete customer record
def delete_customer_record(customer_id):
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    if customer is None:
        return False
    else:
        db.session.delete(customer)
        db.session.commit()
        return True
#-- Update customer record
def update_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy):
    #-- Data check. its only needed in CLI mode. when data populated there is no need for it.
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    if customer is None:
        return False
    else:
        customer.customer_id = customer_id
        customer.first_name = first_name
        customer.last_name = last_name
        customer.address = address
        customer.email = email
        customer.phone = phone
        customer.basket = basket
        customer.buy = buy
        db.session.commit()
        return True
############################# Items

class Item(db.Model):
    #-- Item table
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(100), unique=True)
    model = db.Column(db.String(30),nullable=False)
    serial = db.Column(db.String(30), unique=True, default="N/A")
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.String(255), default="N/A")

    #-- For debuging i use __str__
    # def __repr__(self):
    #     return "<Item %r>" % self.item_id, self.category, self.name, self.quantity, self.price, self.description
    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.item_id, self.category, self.name, self.model, self.serial, self.quantity, self.price, self.description)

def show_all_items():
    all_items = Item.query.all()
    return all_items

def get_item(item_id):
    item = Item.query.filter_by(item_id=item_id).first()
    return item

def insert_item_record(category, name, model, serial, quantity, price, description):
        check_item = Item.query.filter_by(serial=serial).first()
        if check_item is None:
            new_item =  Item(category=category, name=name, model=model, serial=serial, quantity=quantity, price=price, description=description)
            db.session.add(new_item)
            db.session.commit()
            return True
        else:
            return False

#-- Update Item record
def update_item_record(item_id,category, name, model, serial, quantity, price, description):
    #-- Data check. its only needed in CLI mode. when data populated there is no need for it.
    item = Item.query.filter_by(item_id=item_id).first()
    if item is None:
        return False
    else:
        item.item_id = item_id
        item.category = category
        item.name = name
        item.model = model
        item.serial = serial
        item.quantity = quantity
        item.price = price
        item.description = description
        db.session.commit()
        return True

#-- Delete customer record
def delete_item_record(item_id):
    item = Item.query.filter_by(item_id=item_id).first()
    if item is None:
        return False
    else:
        db.session.delete(item)
        db.session.commit()
        return True

#####################################  Item Search functions
def search_category(category):
    items = Item.query.filter_by(category=category).all()
    if len(items) == 0:
        return "404"
    return items

def search_model(model):
    items = Item.query.filter_by(model=model).all()
    if len(items) == 0:
        return "404"
    return items

def search_item_name(item_name):
    items = Item.query.filter_by(name=item_name).all()
    if len(items) == 0:
        return "404"
    return items

def search_price(price):
    items = Item.query.filter_by(price=price).all()
    if len(items) == 0:
        return "404"
    return items

def search_quantity(quantity):
    items = Item.query.filter_by(quantity=quantity).all()
    if len(items) == 0:
        return "404"
    return items

def search_serial(serial):
    items = Item.query.filter_by(serial=serial).all()
    if len(items) == 0:
        return "404"
    return items
