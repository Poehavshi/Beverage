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

    username = db.Column(db.String(64), index=True, unique=True) # логин
    password_hash = db.Column(db.String(128)) # Пароль в виде хеша


    def __repr__(self):
        return f'<Participant {self.username}>' 