from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flaskr.models import Teacher


class TeacherRegisterationForm(FlaskForm):
    title = SelectField(
        "Title",
        choices=[
            ("mr", "Mr"),
            ("mrs", "Mrs"),
            ("miss", "Miss"),
            ("engr", "Engr"),
            ("dr", "Dr"),
        ],
        validators=[DataRequired()],
    )
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    middle_name = StringField("Middle Name")
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    sex = SelectField(
        "Sex", choices=[("m", "Male"), ("f", "Female")], validators=[DataRequired()]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    section = SelectField(
        "Section",
        choices=[
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
            ("junior", "Junior"),
        ],
        validators=[DataRequired()],
    )

    picture = FileField(
        "Upload Student Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    phone_number = StringField("Phone Number")
    address = TextAreaField("Address")
    submit = SubmitField("Register Teacher")

    def validate_email(self, email):
        teacher = Teacher.query.filter_by(email=email.data).first()
        if teacher:
            raise ValidationError(
                "This email is taken by another teacher. Please choose another one!"
            )


class TeacherUpdateForm(FlaskForm):
    title = SelectField(
        "Title",
        choices=[
            ("mr", "Mr"),
            ("mrs", "Mrs"),
            ("miss", "Miss"),
            ("engr", "Engr"),
            ("dr", "Dr"),
        ],
        validators=[DataRequired()],
    )
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    middle_name = StringField("Middle Name")
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=1, max=30)]
    )
    sex = SelectField(
        "Sex", choices=[("m", "Male"), ("f", "Female")], validators=[DataRequired()]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    section = SelectField(
        "Section",
        choices=[
            ("science", "Science"),
            ("commercial", "Commercial"),
            ("art", "Art"),
            ("junior", "Junior"),
        ],
        validators=[DataRequired()],
    )

    picture = FileField(
        "Upload Student Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    phone_number = StringField("Phone Number")
    address = TextAreaField("Address")
    submit = SubmitField("Save Update")

    def validate_email(self, email):
        teacher = Teacher.query.filter_by(email=email.data).first()
        if teacher:
            if email.data != teacher.email:
                raise ValidationError(
                    "This email is taken by another teacher. Please choose another one!"
                )
