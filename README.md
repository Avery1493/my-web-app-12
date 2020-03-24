# my-web-app-12

## RUN APP
# one-time thing, to set the env var
set FLASK_APP=web_app
flask run

## MIGRATE TO DATABASE
# generates app/migrations dir
flask db init 
# creates the db (with "alembic_version" table)
flask db migrate 
# creates the specified tables
flask db upgrade 