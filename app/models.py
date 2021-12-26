'''
Файл с классами-сущностями из базы данных
'''
from app import db

class Participant(db.Model):
    '''
    Сущность участника
    содержит всю необходимую о нем информацию
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64)) # Имя
    surname = db.Column(db.String(64)) # Фамилия
    patronymic = db.Column(db.String(64)) # Отчество
    city = db.Column(db.String(64),index=True) # Город
    description = db.Column(db.String(256)) # Описание-биография
    gender = db.Column(db.Boolean()) # True - male, False - female
    applications = db.relationship('Application', backref='author', lazy='dynamic')

    username = db.Column(db.String(64), index=True, unique=True) # логин
    password_hash = db.Column(db.String(128)) # Пароль в виде хеша


    def __repr__(self):
        return f'<Participant {self.username}>'

class Competition(db.Model):
    '''
    Сущность соревнования
    содержит всю необходимую информацию о соревновании
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True) # Имя
    description = db.Column(db.String(256)) # Описание соревнования
    city = db.Column(db.String(64),index=True) # Город

    applications = db.relationship('Application', backref='competition', lazy='dynamic')

    # Дата начала и конца
    start_date = db.Column(db.DateTime, index = True)
    end_date = db.Column(db.DateTime, index = True)

    def __repr__(self):
        return f'<Competition {self.name}>' 

class Application(db.Model):
    '''
    Сущность соревнования
    содержит всю необходимую информацию о соревновании
    '''
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256)) # Описание соревнования
    rating = db.Column(db.Integer, default = 0) # Выставленные баллы за заявку

    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))

    def __repr__(self):
        return f'<Application {self.id}>' 
