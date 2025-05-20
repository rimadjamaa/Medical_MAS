from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from extentions import db 

bcrypt = Bcrypt()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.password_hash, password)
