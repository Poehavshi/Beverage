'''
Файл с обработкой логики для всех страниц нашего приложения
'''
from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import Participant
from werkzeug.urls import url_parse
from app import db

@app.route('/')
@app.route('/index')
@login_required
def index():
    '''
    Главная страница приложения со списком всех заявок
    '''
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
    return render_template('index.html', title='Home', applications = applications)

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Страница входа для участника по логину и паролю
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Participant.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


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
        user = Participant(
            username=form.username.data, 
            name=form.name.data,
            surname = form.surname.data,
            patronymic = form.patronymic.data,
            city = form.city.data,
            description = form.description.data,
            gender = form.gender.data
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)