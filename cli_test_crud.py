"""
Temporary helper module to interact with database
"""

from models import *

import os

#-- Customer schema
"""
customer_id = db.Column(db.String(13), primary_key=True, autoincrement=True)
first_name = db.Column(db.String(40), nullable=False)
last_name = db.Column(db.String(40), nullable=False)
address = db.Column(db.String(255), nullable=False)
email = db.Column(db.String(80,), nullable=False, unique=True)
phone = db.Column(db.Integer, nullable=False)
basket = db.Column(db.String(40))
buy = db.Column(db.String(40))
"""
#-- User section
#-- Inserting new record to table
def insert_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy):
        # Basic data check by ID if doesnt exists will add the record
        # Ithink data check is only usefull in CLI mode - maybe weneed to remove it late
        check_customer = Customer.query.filter_by(customer_id=customer_id).first()
        if check_customer is None:
            new_customer =  Customer(customer_id = customer_id, first_name=first_name, last_name=last_name, address=address, email=email, phone=phone, basket=basket, buy=buy)
            db.session.add(new_customer)
            db.session.commit()
            print("New record added")
        else:
            print("Record exists")

def remove_customer_record(customer_id):
    #== Data check. its only needed in CLI mode. when data populated there is no need for it.
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    if customer is None:
        print("record not found")
    else:
        db.session.delete(customer)
        db.session.commit()
        print("Record been removed from database")


def update_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy):
    #-- Data check. its only needed in CLI mode. when data populated there is no need for it.
    customer = Customer.query.filter_by(customer_id=customer_id).first()
    if customer is None:
        print("record not found")
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


def show_all_customers():
    all_customers = Customer.query.all()
    for customer in all_customers:
        print(customer) # for web service should be desabled, instead return


#-- Retuns a customer by ID
def search_by_customer_id(customer_id):
    customers = Customer.query.filter_by(customer_id=customer_id).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer

def search_by_customer_address(address):
    customers = Customer.query.filter_by(address=address).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer

def search_by_customer_email(email):
    customers = Customer.query.filter_by(email=email).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer

def search_by_customer_last_name(last_name):
    customers = Customer.query.filter_by(last_name=last_name).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer

def search_by_customer_phone(phone):
    customers = Customer.query.filter_by(phone=phone).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer


def search_by_customer_first_name(first_name):
    customers = Customer.query.filter_by(first_name=first_name).all()
    if len(customers) == 0:
        return False
    else:
        for customer in customers:
            return customer


#-- Item schema
"""
item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
category = db.Column(db.String(100))
name = db.Column(db.String(100), unique=True)
model = db.Column(db.String(30),nullable=False)
serial = db.Column(db.String(30), unique=True)
quantity = db.Column(db.Integer)
price = db.Column(db.Integer)
description = db.Column(db.String(255))
"""
#-- Item section

def insert_item_record(category, name, model, serial, quantity, price, description):
        # Basic data check by ID if doesnt exists will add the record
        new_item =  Item(category=category, name=name, model=model, serial=serial, quantity=quantity, price=price, description=description)
        db.session.add(new_item)
        db.session.commit()


def remove_item_record(item_id):
    item = Item.query.filter_by(item_id=item_id).first()
    if item is None:
        print("record not found")
    else:
        db.session.delete(item)
        db.session.commit()

def update_item_record(item_id, category, name, model, serial, quantity, price, description):
    item = Item.query.filter_by(item_id=item_id).first()
    if item is None:
        print("Record not found")
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

def show_all_items():
    all_items = Item.query.all()
    for item in all_items:
        print(item)
