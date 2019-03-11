#!/usr/bin/env python3

from flask import Flask
myapp = Flask(__name__)

# @myapp.route("/")
# def hello():
#     return "Hello Flask, on Azure App Service for Linux"

@myapp.route('/', defaults={'path': ''})
@myapp.route('/<path:path>')
def hello(path):
    return '<b>Welcome to %s admin page</b>\
    </br>\
			You need the authorization to access this page\
		</br>\
		</br>\
		<form>\
	  		User name:<br>\
	  			<input type="text" name="username"><br>\
	  		User password:<br>\
	  			<input type="password" name="psw">\
		</form>\
  			<input type="submit" value="Submit">' % path