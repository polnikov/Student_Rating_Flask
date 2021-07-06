from flask_wtf import FlaskForm
from flask_wtf.recaptcha import widgets
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.fields.core import DateField, RadioField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя', 
        validators=[DataRequired(),], 
        render_kw={"class": "form-control"}, 
        )
    password = PasswordField(
        'Пароль', 
        validators=[DataRequired()], 
        render_kw={"class": "form-control"}, 
        )
    submit = SubmitField(
        'Вход', 
        render_kw={"class":"btn btn-secondary"}, 
        )

class StudentForm(FlaskForm):
    last_name = StringField(
        'Фамилия', 
        validators=[DataRequired(),], 
        render_kw={"class": "form-control"}, 
        )
    first_name = StringField(
        'Имя', 
        validators=[DataRequired()], 
        render_kw={"class": "form-control"}, 
        )
    second_name = StringField(
        'Отчество', 
        render_kw={"class": "form-control"}, 
        )
    student_id = StringField(
        'Номер зачетной книжки', 
        render_kw={"class": "form-control"}, 
        validators=[DataRequired()], 
        )
    citizenship = RadioField(
        'Гражданство', 
        validators=[DataRequired(),], 
        choices=[
            ('РФ', 'Россия'),
            ('Ин', 'Иностранец'),
        ], 
    )
    basis = RadioField(
        'Основа обучения', 
        validators=[DataRequired(),], 
        choices=[
            ('Б', 'Бюджет'),
            ('К', 'Контракт'),
            ('ИГ', 'ИнГосЛиния'),
        ], 
    )
    level = RadioField(
        'Уровень образования', 
        validators=[DataRequired(),], 
        choices=[
            ('Бак', 'Бакалавриат'),
            ('Маг', 'Магистратура'),
        ], 
    )
    group = RadioField(
        'Группа', 
        validators=[DataRequired(),], 
        choices=[
            ('ТТ', 'ТТ'),
            ('ЭЭ', 'ЭЭ'),
            ('ИС', 'ИС'),
            ('ЗК', 'ЗК'),
            ('ТТм', 'ТТм'),
            ('ЗКм', 'ЗКм'),
            ('ЭЭм', 'ЭЭм'),
            ('ТГВм', 'ТГВм'),
            ('ВВм', 'ВВм'),
        ], 
    )
    start_date = DateField(
        'Дата зачисления [дд.мм.гггг]',
        format='%d-%m-%Y',
    )
    status = RadioField(
        'Текущий статус', 
        validators=[DataRequired(),], 
        choices=[
            ('ЯС', 'Является студентом'),
            ('АО', 'Академический отпуск'),
            ('ОТ', 'Отчислен'),
        ], 
    )
    comment = TextAreaField(
        'Примечание', 
        render_kw={"class": "form-control"}, 
    )
    submit = SubmitField(
        'Добавить', 
        render_kw={"class":"btn btn-secondary"}, 
        )


class SubjectForm(FlaskForm):
    subject_name = StringField(
        'Наименование дисциплины', 
        validators=[DataRequired(),], 
        render_kw={"class": "form-control"}, 
        )
    cathedra = RadioField(
        'Кафедра', 
        choices=[
            ('КАДМиТ', 'автомобильных дорог, мостов и тоннелей'),
            ('КАСК', 'архитектурно-строительных конструкций'),
            ('КВиЭ', 'водопользования и экологии'),
            ('КГЕО', 'геотехники'),
            ('КГЗиК', 'геодезии, землеустройства и кадастров'),
            ('КЖБК', 'железобетонных и каменных конструкций'),
            ('КИТ ', 'информационных технологий'),
            ('КМАТ', 'математики'),
            ('КМиДК', 'металлических и деревянных конструкций'),
            ('КОС', 'организации строительства'),
            ('КСМ', 'строительной механики'),
            ('КСФиХ', 'строительной физики и химии'),
            ('КТГВ', 'теплогазоснабжения и вентиляции'),
            ('КТСМиМ', 'технологии строительных материалов и метрологии'),
            ('КТСП', 'технологии строительного производства'),
            ('КЭиЭ', 'электроэнергетики и электротехники'),
        ]
    )
    teacher = StringField(
        'Преподаватель [Фамилия И.О.]', 
        render_kw={"class": "form-control"}, 
        )
    att_date = DateField(
        'Дата аттестации [дд.мм.гггг]',
        format='%d-%m-%Y',
    )
    comment = TextAreaField(
        'Примечание', 
        render_kw={"class": "form-control"}, 
    )
    submit = SubmitField(
        'Отправить', 
        render_kw={"class":"btn btn-secondary"}, 
        )

