from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import(
    StringField,
    IntegerField
)
from wtforms.validators import (
    DataRequired
)


class MemberEditForm(FlaskForm):
    first_name = StringField(
        validators=[DataRequired()]
    )
    last_name = StringField(
        validators=[DataRequired()]
    )
    role = StringField()
    display_order = IntegerField(
        validators=[DataRequired()]
    )
    cover_img = FileField()
    name_img = FileField()