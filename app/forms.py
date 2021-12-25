'''
Файл с формами ввода для веб приложения
В первую очередь для формы логина
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    '''
    Форма ввода данных пользователя для входа
    Состоит из кнопки Sign In
    И полей ввода с проверкой на наличие данных внутри них
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')