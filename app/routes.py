'''
Файл с обработкой логики для всех страниц нашего приложения
'''
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    '''
    Главная страница приложения со списком всех заявок
    '''
    user = {'name': 'Ivan', 'surname': 'Ivanov'}
    applications = [
        {
            'author': {'name': 'John', 'surname': 'Johness'},
            'description': 'Beautiful day in Portland!'
        },
        {
            'author': {'name': 'Susan', 'surname': 'Susanness'},
            'description': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'name': 'Ипполит', 'surname': 'Ипполитович'},
            'description': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, applications = applications)

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Страница входа для участника по логину и паролю
    '''
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign in', form = form)