import sys
from getpass import getpass

from rating import create_app
from rating.model import User, db

app = create_app()


with app.app_context():
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    
    if not password == password2:
        sys.exit(0)
    
    new_user = User(username=username, role='Администратор')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'Пользователь с id {new_user.id} создан')
