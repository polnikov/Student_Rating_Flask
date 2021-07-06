from flask import Flask, flash, redirect, render_template, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

from rating.forms import LoginForm, StudentForm, SubjectForm
from rating.model import Student, Subject, User, db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def main():
        return render_template('main.html')

    @app.route('/login')
    def login():
        print(current_user)
        if current_user.is_authenticated:
            return redirect(url_for('main'))
        
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', title=title, form=login_form)
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли')
        return redirect(url_for('main'))

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('main'))
        
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'

    @app.route('/students')
    def students():
        title = 'Сведения об обучающихся'
        return render_template('students.html', title=title)

    @app.route('/students/<int:student_id>/')
    def student_detail():
        return render_template('student_detail.html')

    @app.route('/subjects')
    def subjects():
        title = 'Сведения о дисциплинах'
        return render_template('subjects.html', title=title)

    @app.route('/add-student')
    def add_student():
        title = 'Добавить обучающегося'
        student_form = StudentForm()
        return render_template('add_student.html', title=title, form=student_form)
    
    @app.route('/add-subject')
    def add_subject():
        title = 'Добавить дисциплину'
        subject_form = SubjectForm()
        return render_template('add_subject.html', title=title, form=subject_form)
    
    return app

# if __name__ == "__main__":
#     app.run(debug=True)
