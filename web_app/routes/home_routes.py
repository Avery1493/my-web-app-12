
# web_app/routes/home_routes.py

from flask import Blueprint

# import from init file
home_routes = Blueprint("home_routes", __name__)


# attach route to bluprint object instead of app directly
@home_routes.route('/') # home page
def hello_world():
    print("Visit Hello Page")
    return 'Hello, World!'

# about page
@home_routes.route('/about') # about page
def about():
    print("Visit About Page")
    return 'About Me'