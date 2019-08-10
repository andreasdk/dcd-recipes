from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])