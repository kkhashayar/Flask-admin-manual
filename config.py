#-- Flak core classes and methods will destribute from here
from flask import Flask, render_template, url_for, redirect, flash 
#-- for securoty
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_basicauth import BasicAuth


app = Flask(__name__)



#-- configurations
#username = User.query.filet_by(id = i).first()
app.config["BASIC_AUTH_USERNAME"] = "khashayar"
app.config["BASIC_AUTH_PASSWORD"] = "password"
app.config["BASIC_AUTH_FORCE"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_ECHO"] = False # For debug, displays the results
app.config["SECURITY_PASSWORD_HASH"] = "plaintext" # Choosing the method of hashing password


basic_auth = BasicAuth(app)
