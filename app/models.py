import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from app import db

from app import login

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin


from flask import url_for

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(120), default='default_avatar.png')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def avatar_url(self):
        if self.avatar:
            return url_for('static', filename=f'avatars/{self.avatar}')
        return url_for('static', filename='avatars/default_avatar.png')

    def __repr__(self) -> str:
        return f"<User(id={self.id}),(username={self.username})>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    #date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__ (self) -> str:
        return f"<Post(id={self.id})>"
