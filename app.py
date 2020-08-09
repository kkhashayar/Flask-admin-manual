from config import *
from models import *
from forms import *
import os
from flask import request

"""
Home page contains two main pages.
CUSTOMERS and ITEMS. Gives Admin access control over CRUD functionality
Password protected
"""

@app.route("/home")
#@login_required
def home():
    return render_template("home.html")


#-- search routes
#-- Search by ID
@app.route("/search_customer_id", methods=["POST", "GET"])
def search_by_customer_id():
    form = SearchIdForm()
    if form.validate_on_submit():
        id = form.id.data
        results = search_customer_id(id)

        return render_template("customer_results.html", results=results)
    return render_template("search_customer_id.html", form=form)

#-- search by Address
@app.route("/search_customer_address", methods=["GET","POST"])
def search_by_customer_address():
    form = SearchAddressForm()
    if form.validate_on_submit():

        address =form.address.data
        results = search_address(address)
        return render_template("customer_results.html", results=results)

    return render_template("search_customer_address.html", form=form)

#-- Search by First Name
@app.route("/search_customer_firstname", methods=["POST", "GET"])
def search_by_customer_firstname():
    form = SearchFirstNameForm()
    if form.validate_on_submit():

        firstname = form.firstname.data
        results = search_firstname(firstname)
        return render_template("customer_results.html", results=results)

    return render_template("search_customer_firstname.html", form=form)


#-- Search by last Name
@app.route("/search_customer_lastname", methods=["POST", "GET"])
def search_by_customer_lastname():
    form = SearchLastNameForm()
    if form.validate_on_submit():
        lastname = form.lastname.data

        results = search_lastname(lastname)
        return render_template("customer_results.html", results=results)

    return render_template("search_customer_lastname.html", form=form)


#-- Search by email
@app.route("/search_customer_email", methods=["POST", "GET"])
def search_by_customer_email():
    form = SearchEmailForm()
    if form.validate_on_submit():
        email = form.email.data
        results = search_email(email)
        return render_template("customer_results.html", results=results)
    return render_template("search_customer_email.html", form=form)



#-- search by phone
@app.route("/search_customer_phone", methods=["POST", "GET"])
def search_by_customer_phone():
    form = SearchPhoneForm()
    if form.validate_on_submit():
        phone = form.phone.data
        results = search_phone(phone)
        return render_template("customer_results.html", results=results)
    return render_template("search_customer_phone.html", form=form)


##################################################################
#-- Customers CRUD
#-- To display the records we need to create the forms to populate the results
@app.route("/customers", methods=["GET", "POST"])
def customers():
    form = SelectCustomerForm()
    all_customers = show_all_customers()
    return render_template("customers.html", all_customers=all_customers, form=form)

#-- Add new customer
@app.route("/add_new_customer", methods=["GET", "POST"])
def add_new_customer():
    form =  InsertCustomerForm()

    if form.validate_on_submit():
        customer_id = form.customer_id.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        email = form.email.data
        phone = form.phone.data
        basket = form.basket.data
        buy = form.buy.data
        if len(str(abs(customer_id))) < 10:
            return "<h4>ID should be 10 digit</h4>"
        else:
            if insert_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy) is True:
                return customers()
            else:
                return "<h4>Record exists with the same Customer ID</h4>"
    return render_template("add_new_customer.html", form=form)

######################################  Customer search routes

"""
    Customer schema 

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(80,), nullable=False, unique=True)
    phone = db.Column(db.String(30), nullable=False)
    basket = db.Column(db.String(40), nullable=True, default="None")
    buy = db.Column(db.String(40), nullable=True, default="None")
    
"""


#-- Returning a single customer by ID
#-- With Delete and Update functions
@app.route("/<customer_id>", methods=["POST", "GET"])
def customer(customer_id):
    # separating Items and customers 
    if len(customer_id) < 10:
        item_id = customer_id
        return item(item_id)

    #-- Customer crud starts here 

    else:
        customer = get_customer(customer_id)
        form = SelectCustomerForm(customer_id=customer.customer_id,
                                  first_name=customer.first_name, 
                                  last_name=customer.last_name, 
                                  address=customer.address, 
                                  email=customer.email, 
                                  phone=customer.phone, 
                                  basket=customer.basket, 
                                  buy=customer.buy)

        os.system("clear")
        print(customer_id)

        print("getting data from form")
        first_name = form.first_name.data 
        print(first_name)
        #--- all working up to this point 

        #-- Delete the record
        #--if form.validate_on_submit():
        #-- instead of validate on submit i use request.method == "POST"
        if request.method == "POST":
            print("clicked on validate on submit")
            if form.delete.data:
                if delete_customer_record(customer_id) is True:
                    #-- here should go flash and message
                    flash("Record deleted")
                    return customers()
                else:
                    return "<h4>Record doesn't exists</h4>"
            

            #-- Update the record
            #-- everything except Customer ID
            
            elif form.update.data:
                os.system("clear")
                print(customer_id)
                customer_id = form.customer_id.data
                first_name  = form.first_name.data
                last_name = form.last_name.data
                address = form.address.data
                email = form.email.data
                phone = form.phone.data
                basket = form.basket.data
                buy = form.buy.data
                
                if update_customer_record(customer_id, first_name, last_name, address, email, phone, basket, buy) is True:
                    flash("Record updated")
                    return customers()
                else:
                    return "<h4>Record doesn't exists</h4>"

        return render_template("customer.html", form=form)


#-- ************************************************** --#
#-- ************************************************** --#
#-- Item CRUD
@app.route("/items", methods=["POST", "GET"])
def items():
    form = SelectItemForm()
    all_items = show_all_items()
    return render_template("items.html", all_items=all_items, form=form)

#-- Add new Item
@app.route("/add_new_item", methods=["GET", "POST"])
def add_new_item():
    form = InsertItemForm()
    if form.validate_on_submit():
        category = form.category.data
        name = form.name.data
        model = form.model.data
        serial = form.serial.data
        quantity = form.quantity.data
        price = form.price.data
        description = form.description.data
        if insert_item_record(category, name, model, serial, quantity, price, description) is True:
            return items()
        else:
            return "<h4>Record exists with the same serial Number</h4>"


    return render_template("add_new_item.html", form=form)

"""
Item Schema:
item_id = IntegerField("ID")
category = StringField("Category")
name = StringField("Name")
model = StringField("Model")
serial = StringField("Serial")
quantity = IntegerField("Quantity")
price = IntegerField("Price")
description = StringField("Description")
"""

@app.route("/<item_id>", methods=["POST", "GET"])
def item(item_id):
    item = get_item(item_id)
    form = SelectItemForm(item_id=item.item_id, name=item.name, serial=item.serial, quantity=item.quantity, price=item.price)

    #-- Delete the record
    if request.method == "POST":
        if form.delete.data:
            if delete_item_record(item_id) is True:
                #-- here should go flash and message
                flash("Item deleted")
                return items()
            else:
                return "<h4>Record doesn't exists</h4>"
        #-- Update the record
        #-- everything except Customer ID
        if form.update.data:
            item_id = form.item_id.data
            
            name = form.name.data
            
            serial = form.serial.data
            quantity = form.quantity.data
            price = form.price.data
            
            if update_item_record(item_id, name, serial, quantity, price) is True:
                flash("Item updated")
                return items()
            else:
                return "<h4>Record doesn't exists</h4>"

    return render_template("item.html", form=form)


######################################  Item search routes

@app.route("/search_by_category", methods=["POST", "GET"])
def search_by_category():
    form = SearchItemCategoryForm()

    if form.validate_on_submit():
        category = form.category.data
        results = search_category(category)
        return render_template("item_results.html", results=results)

    return render_template("search_item_category.html", form=form)



@app.route("/search_by_model", methods=["POST", "GET"])
def search_by_model():
    form = SearchItemModelForm()

    if form.validate_on_submit():
        model = form.model.data
        results = search_model(model)
        return render_template("item_results.html", results=results)

    return render_template("search_item_model.html", form=form)


@app.route("/search_by_name", methods=["POST", "GET"])
def search_by_name():
    form = SearchItemName()

    if form.validate_on_submit():
        item_name = form.item_name.data
        results = search_item_name(item_name)
        return render_template("item_results.html", results=results)

    return render_template("search_item_name.html", form=form)


@app.route("/search_by_price", methods=["POST", "GET"])
def search_by_price():
    form = SearchItemPrice()

    if form.validate_on_submit():
        price = form.price.data
        results = search_price(price)
        return render_template("item_results.html", results=results)
    return render_template("search_item_price.html", form=form)

@app.route("/search_by_quantity", methods=["POST", "GET"])
def search_by_quantity():
    form = SearchItemQuantityForm()
    if form.validate_on_submit():
        quantity = form.quantity.data
        results = search_quantity(quantity)
        return render_template("item_results.html", results=results)
    return render_template("search_item_quantity.html", form=form)

@app.route("/search_by_serial", methods=["POST", "GET"])
def search_by_serial():
    form = SearchItemSerialForm()
    if form.validate_on_submit():
        serial = form.serial.data
        results = search_serial(serial)
        return render_template("item_results.html", results=results)
    return render_template("search_item_serial.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
