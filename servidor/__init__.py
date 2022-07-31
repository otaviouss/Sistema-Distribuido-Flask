from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////bd/database.db'
db = SQLAlchemy(app)

from servidor.routes import routes