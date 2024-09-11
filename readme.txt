flask db init
flask db migrate
flask db upgrade

Вошел в Python3

>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa


>>> app.app_context().push()

>>> user1 = User(username='Bestuser', email='bestuser@gmail.com', password_hash='1234')
>>> db.session.add(user1)
>>> db.session.commit()

query = sa.select(User)
users = db.session.scalars(query).all()

Вышел из python3



flask db upgrade


inspect.getfullargspec(Class.__init__).args[1:]


from werkzeug.security import check_password_hashuse
from werkzeug.security import generate_password_hash

hash = generate_password_hash('my_password')
check_password_hash(hash, 'abc')
check_password_hash(hash, 'my_password')


user8.set_password('')
user8.check_password('')
user8.check_password('')