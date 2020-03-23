# web_app/__init__.py

# import Flask object
from flask import Flask 

# from web_app.routes.home_routes import home_routes
# from web_app.routes.book_routes import book_routes

def create_app():
    # initilize flask app
    app = Flask(__name__) # app name of file
    # app.register_blueprint(home_routes)
    # app.register_blueprint(book_routes)

    # decorator runs function
    @app.route('/') # home page
    def hello_world():
        print("Visit Hello Page")
        return 'Hello, World!'

    # about page
    @app.route('/about') # about page
    def about():
        print("Visit About Page")
        return 'About Me'

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)