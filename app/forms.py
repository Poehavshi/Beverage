'''
Файл с формами ввода для веб приложения
В первую очередь для формы логина
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Participant

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

class RegistrationForm(FlaskForm):
    '''
    Форма регистрации пользователя в системе
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    name = StringField('Name',validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    patronymic = StringField('Patronymic', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    gender = BooleanField('Male')
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Participant.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')