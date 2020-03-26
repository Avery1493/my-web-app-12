# web_app/__init__.py
import os
from dotenv import load_dotenv


# import Flask object
from flask import Flask 
from web_app.models import db, migrate

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.iris_stats_routes import iris_stats_routes
from web_app.routes.stats_routes import stats_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="sqlite:///web_app_12.db")

def create_app():
    # initilize flask app
    app = Flask(__name__) # name of file

    # configure database to work with application 
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprint so app will know of routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(iris_stats_routes)
    app.register_blueprint(stats_routes)

    return app

if __name__ == "__main__":
    # run app
    my_app = create_app()
    my_app.run(debug=True)