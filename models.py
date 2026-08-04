from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String, unique = True, nullable = False)
    role = db.Column(db.String, nullable = False)
    f_name = db.Column(db.String, nullable = False)
    l_name = db.Column(db.String, nullable = True)
    status = db.Column(db.String, default = 'Pending')
    password = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.String, unique = True, nullable = False) 
    isBlackListed =db.Column(db.Boolean, default = False)

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

class Trek(db.Model):

    __tablename__ = 'treks'
    trek_id = db.Column(db.Integer, primary_key = True, autonincrement = True)
    trek_name = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
    start_date = db.Column(db.DateTime, default = datetime.now)
    end_date = db.Column(db.DateTime, default = datetime.now)
    duration = db.Column(db.Integer, nullable = False)
    difficulty = db.Column(db.String, nullable = False)
    guide_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = True)
    total_slots = db.Column(db.Integer, nullable = False)
    available_slots = db.Column(db.Integer, nullable = True)
    trek_status = db.Column(db.String, nullable = False, default = 'Pending')