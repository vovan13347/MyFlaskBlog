from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.models import Post, User

from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import db

from app.forms import RegistrationForm

from urllib.parse import urlsplit



import logging

from werkzeug.utils import secure_filename
import os
from flask import current_app


logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('test.log') # creates handler for the log file
logger.addHandler(handler) # adds handler to the werkzeug WSGI logger




@app.route('/')
@app.route('/index')
@login_required
def index():
    app.logger.info('Проверка')
    user = {'username': 'User'}
    posts = Post.query.all()
    return render_template('index.html', 
                           title='Home', 
                           user=user, 
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():

    logger.info('Проверка логгера')

    if current_user.is_authenticated:
        return redirect(url_for('user', username=current_user.username))
    
    logger.info('Пользователь не аутентифицирован')

    form = LoginForm()
    if form.validate_on_submit():

        logger.info('Ветвление validate_on_sumbit сработало')

        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        
        logger.info('База данных открылась')
        logger.info('Пользователь: ', form.username.data)
        logger.info('Пароль: ', form.password.data)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('user', username=user.username))
    
    return render_template('login.html', title='Войти', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():

        avatar_filename = None
        if form.avatar.data:
            avatar_file = form.avatar.data
            avatar_filename = secure_filename(avatar_file.filename)
            avatar_path = os.path.join(current_app.root_path, 'static/avatars', avatar_filename)
            avatar_file.save(avatar_path)

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)


        if avatar_filename:
            user.avatar = avatar_filename

        db.session.add(user)
        db.session.commit()
        flash('Спасибо за регистрацию!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = Post.query.filter_by(user_id=user.id).all()
    return render_template('user.html', user=user, posts=posts)
