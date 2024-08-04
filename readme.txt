Вошел в Python3

from app import app, db
from app.models import User, Post
import sqlalchemy

user1 = User(username='Bestuser', email='bestuser@gmail.com', password_hash='1234')
db.session.add(user1)
db.session.commit()


Вышел из python3



flask db upgrade