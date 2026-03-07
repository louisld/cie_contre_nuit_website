from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    PasswordField
)
from wtforms.validators import (
    DataRequired
)


class LoginForm(FlaskForm):
    username = StringField(
        validators=[DataRequired()]
    )
    password = PasswordField(
        validators=[DataRequired()]
    )