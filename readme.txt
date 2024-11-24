flask db init
flask db migrate
flask db upgrade

Вошел в Python3

>>> from app import app, db
>>> from app.models import User, Post
>>> import sqlalchemy as sa
from werkzeug.security import generate_password_hash


>>> app.app_context().push()
user1 = User(username='user1', email='user1@gmail.com', password_hash= generate_password_hash('a123'))
>>> db.session.add(user1)
>>> db.session.commit()

db.session.delete(me)
db.session.commit()

query = sa.select(User)
users = db.session.scalars(query).all()

>>> post1 = Post(title ='title1', text ='user1 create post1', date ='2020-04-28',user_id = 1)
>>> db.session.add(post1)
>>> db.session.commit()

query2 = sa.select(Post)
posts = db.session.scalars(query2).all()

Вышел из python3



flask db upgrade


inspect.getfullargspec(Class.__init__).args[1:]


from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

hash = generate_password_hash('my_password')
check_password_hash(hash, 'abc')
check_password_hash(hash, 'my_password')


user8.set_password('')
user8.check_password('')
user8.check_password('')

pip install flask-login

# helloworlder
# пароль: 1

# https://www.jetbrains.com/datagrip/
# https://dbeaver.io/

# https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/queries.html


sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
sudo sh -c "iptables-save > /etc/iptables/rules.v4"

curl localhost:5000

sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
sudo iptables -I INPUT -p udp --dport 5000 -j ACCEPT


sudo ufw status
sudo iptables -L
sudo systemctl status firewalld



sudo netstat -tuln
flask run --host=0.0.0.0 --port=5000

export FLASK_RUN_HOST=0.0.0.0

git pull origin master


coomit
