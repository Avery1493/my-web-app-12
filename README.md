# my-web-app-12

## RUN APP
# one-time thing, to set the env var
# WINDOWS
set FLASK_APP=web_app  
flask run

## MIGRATE TO DATABASE
# generates app/migrations dir
flask db init 
# creates the db (with "alembic_version" table)
flask db migrate 
# creates the specified tables
flask db upgrade 

# INSTALL PACKAGES
pipenv install Flask Flask-SQLAlchemy Flask-Migrate  
pipenv install python-dotenv requests basilica tweepy  
pipenv install scikit-learn
pipenv install gunicorn psycopg2-binary


# Deploy to HEROKU
# Heroku commands
'''
Procfile
web: gunicorn "web_app:create_app()"
'''

heroku login
heroku apps

git remote -v
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku config
heroku logs
heroku logs --tail

heroku run "FLASK_APP=web_app flask db init"
heroku run "FLASK_APP=web_app flask db stamp head"
heroku run "FLASK_APP=web_app flask db migrate"
heroku run "FLASK_APP=web_app flask db upgrade"