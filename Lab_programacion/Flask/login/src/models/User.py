from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username    
        self.password = generate_password_hash(password)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)