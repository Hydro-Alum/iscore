from flask import abort, session
from datetime import datetime
from sqlalchemy import desc
from flaskr import db, login_manager
from flask_login import UserMixin


# TODO: to implement loader for teacher and student
# @login_manager.user_loader
# def load_user(user_id):
#     management = Management.query.get(int(user_id))
#     teacher = Teacher.query.get(int(user_id))
#     student = Student.query.get(int(user_id))
#     if management:
#         return management
#     elif student:
#         return student
#     elif teacher:
#         return teacher
#     else:
#         abort(404)


# @login_manager.user_loader
# def load_user(user_id):
#     # Try to load user from each table
#     for user_model in [Management, Teacher, Student]:
#         user = user_model.query.get(int(user_id))
#         if user:
#             print("user from model is:", user.role)
#             return user
#     return None


@login_manager.request_loader
def load_user_from_request(request):
    # Extract email from request (e.g., session, cookies, headers, etc.)
    email = session.get("email") or request.args.get("email")
    print(f"got email from login manager: {email}")

    if not email:
        return None

    # Try to load user from each table
    for user_model in [Management, Teacher, Student]:
        user = user_model.query.filter_by(email=email).first()
        print(f"user is {user}")
        if user:
            return user
    return None


class Management(db.Model, UserMixin):
    __tablename__ = "managements"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(20), nullable=False, default="default.jpg")
    role = db.Column(db.String(8), nullable=False, default="admin")

    def __repr__(self):
        return f"Management('{self.first_name}', '{self.email}')"


class Student(db.Model, UserMixin):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    sID = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sex = db.Column(db.String(6), nullable=False)
    email = db.Column(db.String(120), nullable=True, unique=True)
    password = db.Column(db.String(60), nullable=False)
    department = db.Column(db.String(60), nullable=False)
    student_class = db.Column(db.String(60), nullable=False)
    parent_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)
    picture = db.Column(db.String(20), nullable=False, default="default.jpg")
    role = db.Column(db.String(8), nullable=False, default="student")
    results = db.relationship(
        "Result", backref="student", cascade="all, delete-orphan", lazy=True
    )

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.sID}')"


class Teacher(db.Model, UserMixin):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    tID = db.Column(db.String(20), unique=True)
    title = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    section = db.Column(db.String(120), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    sex = db.Column(db.String(6), nullable=False)
    active = db.Column(db.Boolean, default=True)
    picture = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(8), nullable=False, default="teacher")

    def __repr__(self):
        return f"Teacher('{self.first_name}', '{self.email}')"


class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120), nullable=False)
    test_score = db.Column(db.String, nullable=True)
    practical_score = db.Column(db.String, nullable=True)
    exam_score = db.Column(db.String, nullable=True)
    total_score = db.Column(db.String, nullable=True)
    term = db.Column(db.String(120), nullable=False)
    session = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)

    def __repr__(self):
        return f"Result('{self.student}', '{self.subject}')"


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    class_range = db.Column(db.String(50), nullable=False)

    @staticmethod
    def school_subject():
        subjects = Subject.query.all()
        new_subjects = []
        for subject in subjects:
            new_subjects.append((subject.name.replace(" ", "-").lower(), subject.name))
        return new_subjects

    def __repr__(self):
        return f"Subject('{self.name}')"


class SchoolSession(db.Model):
    __tablename__ = "school_sessions"
    id = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)

    @staticmethod
    def school_session():
        current_session = SchoolSession.query.order_by(
            desc(SchoolSession.start_date)
        ).first()
        school_session = []
        if current_session:
            recent_session = int(current_session.session[:4])
        else:
            recent_session = 2024
        for count in range(1, 6):
            each_session = f"{recent_session + count}/{recent_session + count + 1}"
            school_session.append((each_session, each_session))

        return school_session

    def __repr__(self):
        return f"Session('{self.session}', '{self.start_date}')"


class Term(db.Model):
    __tablename__ = "terms"
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Term('{self.term}', '{self.start_date}')"
