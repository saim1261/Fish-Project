from flask import flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(_name_)
app.config("SQLALCHEMY_DATABASE_URI") = "mysql+pymysql://root:roots/flask_db"
app.config["SECRET_KEY"] = "CFDGXTVHJBKNL"

db = SQLAlchemy(app)

from application import routes
