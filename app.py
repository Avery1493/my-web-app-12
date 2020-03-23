
# app.py

# import Flask object
from flask import Flask

# initilize flask app 
app = Flask(__name__) # app name of file


# decorator runs function
@app.route('/') # home page
def hello_world():
    print("Visit Hello Page")
    return 'Hello, World!'

# 
@app.route('/about') # about page
def about():
    print("Visit About Page")
    return 'About Me'