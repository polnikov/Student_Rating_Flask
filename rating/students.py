from rating.model import Student, db


def save_students(
    student_id, 
    last_name, 
    first_name, 
    second_name, 
    basis, 
    citizenship, 
    level, 
    group, 
    start_date, 
    status, 
    comment
    ):
    student_exists = Student.query.filter(Student.student_id == student_id).count()
    if not student_exists:
        new_student = Student(
            student_id, 
            last_name, 
            first_name, 
            second_name, 
            basis, 
            citizenship, 
            level, 
            group, 
            start_date, 
            status, 
            comment
            )
        db.session.add(new_student)
        db.session.commit()
