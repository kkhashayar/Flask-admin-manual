#-- Flask-wtf module, classes and methods
from config import *
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


#-- Customer forsm
"""
id = db.Column(db.String(13), primary_key=True)
first_name = db.Column(db.String(40), nullable=False)
last_name = db.Column(db.String(40), nullable=False)
address = db.Column(db.String(255), nullable=False)
email = db.Column(db.String(80,), nullable=False, unique=True)
phone = db.Column(db.Integer, nullable=False)
basket = db.Column(db.String(40), nullable=True, default="None")
buy = db.Column(db.String(40), nullable=True, default="None")
"""


class SelectCustomerForm(FlaskForm):
    customer_id = IntegerField("Customer ID")
    first_name = StringField("First name")
    last_name = StringField("Last name")
    address = StringField("Address")
    email = StringField("Email")
    phone = StringField("Phone")
    basket = StringField("Basket")
    buy = StringField("Buy")
    delete = SubmitField(label="DELETE")
    update = SubmitField(label="UPDATE")


class InsertCustomerForm(FlaskForm):
    customer_id = IntegerField("Customer ID")
    first_name = StringField("First name")
    last_name = StringField("Last name")
    address = StringField("Address")
    email = StringField("Email")
    phone = StringField("Phone")
    basket = StringField("Basket")
    buy = StringField("Buy")
    submit = SubmitField("ADD")

#-- individual search forms for Customer
class SearchAddressForm(FlaskForm):
    address = StringField("Address")
    submit = SubmitField("Search")

class SearchIdForm(FlaskForm):
    id = IntegerField("ID")
    submit = SubmitField("Search")

class SearchFirstNameForm(FlaskForm):
    firstname = StringField("First Name")
    submit = SubmitField("Search")

class SearchLastNameForm(FlaskForm):
    lastname = StringField("last name")
    submit = SubmitField("Search")

class SearchPhoneForm(FlaskForm):
    phone = StringField("Phone")
    submit = SubmitField("Search")

class SearchEmailForm(FlaskForm):
    email = StringField("Email")
    submit = SubmitField("Search")
#-- Item Forms
"""
id = db.Column(db.Integer, primary_key=True)
category = db.Column(db.String(100))
name = db.Column(db.String(100), unique=True)
model = db.Column(db.String(30),nullable=False)
serial = db.Column(db.String(30), unique=True, default="N/A")
quantity = db.Column(db.Integer)
price = db.Column(db.Integer)
description = db.Column(db.String(255), default="N/A")
"""

class SelectItemForm(FlaskForm):
    item_id = IntegerField("Item ID")
    #category = StringField("Category")
    name = StringField("Name")
    #model = StringField("Model")
    serial = StringField("Serial")
    quantity = IntegerField("Quantity")
    price = IntegerField("Price")
    #description = StringField("Description")
    delete = SubmitField(label="DELETE")
    update = SubmitField(label="UPDATE")

class InsertItemForm(FlaskForm):
    category = StringField("Category")
    name = StringField("name")
    model = StringField("Model")
    serial = StringField("Serial")
    quantity = IntegerField("Quantity")
    price = StringField("Price")
    description = StringField("Description")
    submit = SubmitField("ADD")

#-- Individual search forms for Item

class SearchItemCategoryForm(FlaskForm):
    category = StringField("Category")
    submit = SubmitField("Search")

class SearchItemName(FlaskForm):
    item_name = StringField("Name")
    submit =SubmitField("Search")

class SearchItemModelForm(FlaskForm):
    model = StringField("Model")
    submit = SubmitField("search")

class SearchItemSerialForm(FlaskForm):
    serial = StringField("Serial")
    submit = SubmitField("Search")

class SearchItemQuantityForm(FlaskForm):
    quantity = IntegerField("Quantity")
    submit = SubmitField("Search")

class SearchItemPrice(FlaskForm):
    price = IntegerField("Price")
    submit = SubmitField("Search")
