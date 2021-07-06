from rating.model import Subject, db


def save_subjects(subject_name, cathedra, teacher, att_date, comment):
    new_subject = Subject(
        subject_name=subject_name,
        cathedra=cathedra,
        teacher=teacher,
        att_date=att_date,
        comment=comment,
    )
    db.session.add(new_subject)
    db.session.commit()
