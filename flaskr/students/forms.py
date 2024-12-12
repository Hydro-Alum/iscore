from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flaskr.models import Student


class StudentRegisterationForm(FlaskForm):
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    middle_name = StringField("Middle Name")
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    dob = DateField("Date of Birth", validators=[DataRequired()], format="%Y-%m-%d")
    sex = SelectField(
        "Sex", choices=[("m", "Male"), ("f", "Female")], validators=[DataRequired()]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    student_class = SelectField(
        "Class",
        choices=[
            ("JS1", "JSS-1"),
            ("JS2", "JSS-2"),
            ("JS3", "JSS-3"),
            ("SS1", "SSS-1"),
            ("SS2", "SSS-2"),
            ("SS3", "SSS-3"),
        ],
        validators=[DataRequired()],
    )
    department = SelectField(
        "Department",
        choices=[
            ("none", "None"),
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
        ],
        validators=[DataRequired()],
    )
    picture = FileField(
        "Upload Student Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    parent_number = StringField("Parent Phone Number")
    address = TextAreaField("Address")
    submit = SubmitField("Register Student")

    def validate_email(self, email):
        student = Student.query.filter_by(email=email.data).first()
        if student:
            raise ValidationError(
                "This email is taken by another student. Please choose another one!"
            )


class StudentScoreTargetForm(FlaskForm):
    session = SelectField(
        "Academic Session",
        choices=[
            ("current_session", "Current Sesssion"),
        ],
        validators=[DataRequired()],
    )
    term = SelectField(
        "Term",
        choices=[
            ("1st", "First-Term"),
            ("2nd", "Second-Term"),
            ("3rd", "Third-Term"),
        ],
        validators=[DataRequired()],
    )
    # mode = SelectField(
    #     "Test/Exam/Practical",
    #     choices=[
    #         ("test", "Test"),
    #         ("exam", "Exam"),
    #         ("practical", "Practical"),
    #     ],
    #     validators=[DataRequired()],
    # )
    student_class = SelectField(
        "Class",
        choices=[
            ("JS1", "JSS-1"),
            ("JS2", "JSS-2"),
            ("JS3", "JSS-3"),
            ("SS1", "SSS-1"),
            ("SS2", "SSS-2"),
            ("SS3", "SSS-3"),
        ],
        validators=[DataRequired()],
    )
    department = SelectField(
        "Department",
        choices=[
            ("none", "None"),
            ("all", "All"),
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
        ],
        validators=[DataRequired()],
    )
    subject = SelectField(
        "Subject",
        choices=[],
        validators=[DataRequired()],
    )
    submit = SubmitField("Access Score Board")


class StudentResultOptionForm(FlaskForm):
    session = SelectField(
        "Academic Session",
        choices=[
            ("current_session", "Current Sesssion"),
        ],
        validators=[DataRequired()],
    )
    term = SelectField(
        "Term",
        choices=[
            ("1st", "First-Term"),
            ("2nd", "Second-Term"),
            ("3rd", "Third-Term"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Check Result")


class StudentUpdateForm(FlaskForm):
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    middle_name = StringField("Middle Name")
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    dob = DateField("Date of Birth", validators=[DataRequired()], format="%Y-%m-%d")
    sex = SelectField(
        "Sex", choices=[("m", "Male"), ("f", "Female")], validators=[DataRequired()]
    )
    email = StringField(
        "Email",
        render_kw={"placeholder": "Email"},
    )
    student_class = SelectField(
        "Class",
        choices=[
            ("JS1", "JSS-1"),
            ("JS2", "JSS-2"),
            ("JS3", "JSS-3"),
            ("SS1", "SSS-1"),
            ("SS2", "SSS-2"),
            ("SS3", "SSS-3"),
        ],
        validators=[DataRequired()],
    )
    department = SelectField(
        "Department",
        choices=[
            ("none", "None"),
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
        ],
        validators=[DataRequired()],
    )
    picture = FileField(
        "Upload Student Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    parent_number = StringField("Parent Phone Number")
    address = TextAreaField("Address")
    submit = SubmitField("Save Update")

    def validate_email(self, email):
        student = Student.query.filter_by(email=email.data).first()
        if student:
            if email.data != student.email:
                raise ValidationError(
                    "This email is taken by another student. Please choose another one!"
                )


class SubjectScoresOptionForm(FlaskForm):
    session = SelectField(
        "Academic Session",
        choices=[
            ("current_session", "Current Sesssion"),
        ],
        validators=[DataRequired()],
    )
    term = SelectField(
        "Term",
        choices=[
            ("1st", "First-Term"),
            ("2nd", "Second-Term"),
            ("3rd", "Third-Term"),
        ],
        validators=[DataRequired()],
    )
    subject = SelectField(
        "Select Subject",
        choices=[],
        validators=[DataRequired()],
    )
    student_class = SelectField(
        "Class",
        choices=[
            ("JS1", "JSS-1"),
            ("JS2", "JSS-2"),
            ("JS3", "JSS-3"),
            ("SS1", "SSS-1"),
            ("SS2", "SSS-2"),
            ("SS3", "SSS-3"),
        ],
        validators=[DataRequired()],
    )
    department = SelectField(
        "Department",
        choices=[
            ("none", "None"),
            ("all", "All"),
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("View Score")
