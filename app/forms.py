from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User



import logging


logger_forms = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('testforms.log') # creates handler for the log file
logger_forms.addHandler(handler) # adds handler to the werkzeug WSGI logger

class LoginForm(FlaskForm):
    username = StringField('Логин полfьзозателя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')

def validate_username(self, username):
    logger_forms.info('validate_username сработало')
    user = db.session.scalar(sa.select(User).where(
    User.username == username.data))
    logger_forms.info('База данных открылась')
    if user is not None:
        logger_forms.info('user is not None')
        raise ValidationError('Неправильное имя пользователя или пароль.')
    
def validate_password(self, password):
    user = db.session.scalar(sa.select(User).where(
        User.password_hash == password.data))
    if user is not None:
        raise ValidationError('Неправильное имя пользователя или пароль.')
    


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Имя пользователя введено неправильно')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Email введен неправильно')