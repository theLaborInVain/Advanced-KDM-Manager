from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Optional(strip_whitespace=True)
    ])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('LOGIN')
