from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
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