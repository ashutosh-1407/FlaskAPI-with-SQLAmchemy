from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
conn_string = 'postgresql://postgres:postgres@database:5432/mydb'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
