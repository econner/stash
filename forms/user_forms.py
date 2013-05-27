from wtforms import Form
from wtforms import PasswordField
from wtforms import TextField
from wtforms import validators

from core.logic import registration_logic


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.Required(),
                                              validators.Length(min=6)])

    def validate_username(self, field):
        valid, message = registration_logic.check_username(field.data)
        if not valid:
            raise validators.ValidationError(message)

    def validate_email(self, field):
        valid, message = registration_logic.check_email(field.data)
        if not valid:
            raise validators.ValidationError(message)


class LoginForm(Form):
    username_or_email = TextField('Username or Email',
                                  [validators.Length(min=4, max=35)])
    password = PasswordField('Password', [validators.Required(),
                                          validators.Length(min=6)])
