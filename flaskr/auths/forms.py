from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
        ],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        "password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"},
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
