"""

    In this module, we manage three forms for the login application:

        - LoginForm: the normal login form for existing users
        - SignupForm: the form that creates a new user
        - ResetForm: the form for resetting a lost/forgotten password

    Don't do anything in this module that doesn't relate to those.

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

class LoginForm(FlaskForm):

    """ This one is pretty basic: we're requiring all fields, stripping
        space and passing a bool for 'remember me', which flask-login will
        eventually use. """

    username = StringField('Username', validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Optional(strip_whitespace=True)
    ])

    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('LOGIN')
