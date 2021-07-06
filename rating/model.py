import enum
from datetime import datetime
from operator import index

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(
        db.Integer, 
        primary_key=True,
        )
    student_id = db.Column(
        db.Integer, 
        nullable=False, 
        unique=True,
        index=True,
        )
    last_name = db.Column(
        db.String(30), 
        nullable=False, 
        index=True,
        )
    first_name = db.Column(
        db.String(30), 
        nullable=False,
        )
    second_name = db.Column(
        db.String(30), 
        nullable=True,
        )


    class StudentBasisEnum(enum.Enum):
        BASIS = (
            ('Б', 'Бюджет'),
            ('К', 'Контракт'),
            ('ИГ', 'ИнГосЛиния'),
        )


    basis = db.Column(
        db.Enum(StudentBasisEnum), 
        nullable=False,
        default='Б',
        )


    class StudentCitizenshipEnum(enum.Enum):
        CITIZENSHIP = (
            ('РФ', 'Россия'),
            ('Ин', 'Иностранец'),
        )


    citizenship = db.Column(
        db.Enum(StudentCitizenshipEnum), 
        nullable=False,
        default='Россия',
        )


    class StudentLevelEnum(enum.Enum):
        LEVEL = (
            ('Бак', 'Бакалавриат'),
            ('Маг', 'Магистратура'),
        )


    level = db.Column(
        db.Enum(StudentLevelEnum), 
        nullable=False,
        )


    class StudentGroupEnum(enum.Enum):
        GROUP = (
            ('ТТ', 'ТТ'),
            ('ЭЭ', 'ЭЭ'),
            ('ИС', 'ИС'),
            ('ЗК', 'ЗК'),
            ('ТТм', 'ТТм'),
            ('ЗКм', 'ЗКм'),
            ('ЭЭм', 'ЭЭм'),
            ('ТГВм', 'ТГВм'),
            ('ВВм', 'ВВм'),
        )


    group = db.Column(
        db.Enum(StudentGroupEnum), 
        nullable=False,
        )
    start_date = db.Column(
        db.Date, 
        nullable=False, 
        )


    class StudentStatusEnum(enum.Enum):
        STATUS = (
            ('ЯС', 'Является студентом'),
            ('АО', 'Академический отпуск'),
            ('ОТ', 'Отчислен'),
        )


    status = db.Column(
        db.Enum(StudentStatusEnum), 
        nullable=False,
        default='Является студентом',
        )
    comment = db.Column(
        db.Text(255), 
        nullable=True,
        default='',
        )
    created_date = db.Column(
        db.DateTime(), 
        default=datetime.utcnow
        )
    updated_date  = db.Column(
        db.DateTime(), 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow,
        )
    
    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'
    
    # def get_absolute_url(self):
    #     return reverse('students:student_detail', args=[str(self.student_id)])
    
    def __repr__(self):
        return f'Студент: {self.last_name} {self.first_name} {self.second_name} / {self.student_id}'


class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(
        db.Integer, 
        primary_key=True,
        )
    subject_name = db.Column(
        db.String(150), 
        nullable=False, 
        index=True,
        )
    
    
    class CathedraEnum(enum.Enum):
        CATHEDRA = [
        ('', ('------', '------')),
        ('ФИЭиГХ', (
            ('КВиЭ', 'водопользования и экологии'),
            ('КГЗиК', 'геодезии, землеустройства и кадастров'),
            ('КСФиХ', 'строительной физики и химии'),
            ('КТГВ', 'теплогазоснабжения и вентиляции'),
            ('КЭиЭ', 'электроэнергетики и электротехники'),
        )
        ),
        ('СФ', (
            ('КАДМиТ', 'автомобильных дорог, мостов и тоннелей'),
            ('КАСК', 'архитектурно-строительных конструкций'),
            ('КГЕО', 'геотехники'),
            ('КЖБК', 'железобетонных и каменных конструкций'),
            ('КИТ ', 'информационных технологий'),
            ('КМиДК', 'металлических и деревянных конструкций'),
            ('КМАТ', 'математики'),
            ('КОС', 'организации строительства'),
            ('КСМ', 'строительной механики'),
            ('КТСП', 'технологии строительного производства'),
            ('КТСМиМ', 'технологии строительных материалов и метрологии'),
        )
        ),
    ]


    cathedra = db.Column(
            db.Enum(CathedraEnum), 
            nullable=True,
            )
    teacher = db.Column(
        db.String(150), 
        nullable=True, 
        index=True,
        )
    att_date = db.Column(
        db.Date, 
        nullable=False, 
        )
    comment = db.Column(
        db.Text(255), 
        nullable=True,
        default='',
        )
    created_date = db.Column(
        db.DateTime(), 
        default=datetime.utcnow
        )
    updated_date  = db.Column(
        db.DateTime(), 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow,
        )
    
    @property
    def empty_att_date(self):
        if self.att_date == None:
            return 'Не назначена'
        else:
            return f'{self.att_date}'

    @property
    def empty_teacher(self):
        if self.teacher == '':
            return 'Не назначен'
        else:
            return f'{self.teacher}'
    
    # def get_absolute_url(self):
    #     return reverse('subject_detail', args=[str(self.id)])
    
    def __repr__(self):
        return f'Дисциплина: {self.subject_name} / {self.cathedra} {self.teacher}'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    created_date = db.Column(
        db.DateTime(), 
        default=datetime.utcnow
        )
    updated_date  = db.Column(
        db.DateTime(), 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow,
        )

    def __repr__(self):
        return f'Пользователь: {self.username} [id: {self.id}]'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'
