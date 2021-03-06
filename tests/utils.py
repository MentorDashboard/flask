from datetime import date, timedelta

from app import db
from app.models.User import create_user
from app.models.Student import create_student, create_student_session


def add_user(name="Test User", email="user@test.com", password="test1234"):
    return create_user(name, email, password)


def add_admin(name="Admin User", email="admin@test.com", password="test1234"):
    user = create_user(name, email, password)
    user.is_admin = True
    db.session.commit()

    return user


def login_user(client, email=None, password=None):
    if email is None and password is None:
        email = "user@test.com"
        password = "test1234"
        add_user("Test User", email, password)

    return client.post("/login", data=dict(email=email, password=password))


def add_student(user, name, email, course, stage):
    student = create_student(name, email, course, stage, user.id)
    student.last_contact = date.today() - timedelta(days=1)
    db.session.commit()

    return student


def add_student_session(student):
    session = create_student_session(
        student.id,
        date.today(),
        45,
        "inception",
        "UCFD",
        "This was an intro call for UCFD",
        "average",
        "",
        "",
    )

    db.session.add(session)
    db.session.commit()

    return session
