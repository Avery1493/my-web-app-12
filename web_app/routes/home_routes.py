
# web_app/routes/home_routes.py

from flask import Blueprint, render_template

# import from init file
home_routes = Blueprint("home_routes", __name__)


# home page
@home_routes.route('/') # home page
def index():
    print("Visit the Prediction Page")
    return render_template("layout.html") 

@home_routes.route('/predict') # home page
def predict():
    print("Visit the Prediction Page")
    return render_template("predict.html")

# attach route to blueprint object instead of app directly
@home_routes.route('/hello')
def hello_world():
    print("Visit Hello Page")
    return 'Hello, World!'

# about page
@home_routes.route('/about') # about page
def about():
    print("Visit About Page")
    return 'About Me'