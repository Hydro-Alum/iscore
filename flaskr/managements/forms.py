from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo, Length
from flaskr.models import SchoolSession


class SchoolSessionForm(FlaskForm):
    session = SelectField(
        "Session",
        choices=[
            ("2023/2024", "2023/2024"),
        ],
        validators=[DataRequired()],
    )
    confirm_session = SelectField(
        "Confirm Session",
        choices=[
            ("2023/2024", "2023/2024"),
        ],
        validators=[DataRequired(), EqualTo("session")],
    )
    start_date = DateField("Begins", validators=[DataRequired()], format="%Y-%m-%d")
    end_date = DateField("Ends", validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField("Create New Session")


class SubjectForm(FlaskForm):
    name = StringField(
        "Subject Name", validators=[DataRequired(), Length(min=1, max=50)]
    )
    class_range = SelectField(
        "Class Range",
        choices=[
            ("all", "All-Student"),
            ("JS", "Junior Students"),
            ("SS", "All Senior Students"),
            ("science", "Senior Science Students"),
            ("commercial", "Senior Commercial Students"),
            ("art", "Senior Art Students"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add New Subject")
