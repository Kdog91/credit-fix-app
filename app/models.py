from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    credit_score = db.Column(db.Integer, nullable=False, default=500)  # Default score

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', Credit Score: {self.credit_score})"
