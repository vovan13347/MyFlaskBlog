from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Имя пользозателя', validators=[DataRequired()])
  password = PasswordField('Пароль', validators=[DataRequired()])
  remember_me = BooleanField('Запомнить')
  submit = SubmitField('Войти')