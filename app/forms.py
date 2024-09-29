from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Логин пользозателя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')

def validate_username(self, username):
    user = db.session.scalar(sa.select(User).where(
    User.username == username.data))
    if user is not None:
        raise ValidationError('Неправильное имя пользователя или пароль.')
    
def validate_email(self, email):
    user = db.session.scalar(sa.select(User).where(
        User.email == email.data))
    if user is not None:
        raise ValidationError('Неправильный email.')