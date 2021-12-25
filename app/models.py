from app import db

'''
    • Уникальный номер — ID;
    • Имя;
    • Фамилия;
    • Отчество;
    • Город проживания;
    • Описание-биография;
    • Пол;
    • Логин;
    • Пароль.
    '''
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64)) # Имя
    surname = db.Column(db.String(64)) # Фамилия
    patronymic = db.Column(db.String(64)) # Отчество
    city = db.Column(db.String(64),index=True) # Город
    description = db.Column(db.String(256)) # Описание-биография
    gender = db.Column(db.Boolean()) # True - m, False - f

    username = db.Column(db.String(64), index=True, unique=True) # логин
    password_hash = db.Column(db.String(128)) # Пароль в виде хеша


    def __repr__(self):
        return f'<Participant {self.username}>' 