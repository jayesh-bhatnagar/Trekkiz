from models import db
from flask import Flask
from helpers import create_admin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pass'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db.init_app(app)
with app.app_context():
    db.create_all()
    create_admin()

from routes import *

if __name__ == '__main__':
    app.run(debug = True, port = 5100)