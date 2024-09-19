from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Iniciar sesión')