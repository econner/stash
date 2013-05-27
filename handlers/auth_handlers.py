from flask import redirect
from flask import request
from flask import url_for
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user

from app import app
from core.logic import registration_logic
from forms.user_forms import LoginForm
from forms.user_forms import RegistrationForm
from messages import error_messages
from models.user_model import User
from utils.response_utils import json_failure
from utils.response_utils import json_success


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user_id = registration_logic.register_user(form)
        user = User.objects.get(pk=user_id)
        login_user(user)
        return redirect(url_for('index'))
    else:
        print form.errors
        return 'Registration Failed. %s' % str(form.errors)


@app.route('/user/validate')
def validate_user():
    username = request.args.get("username")
    if username:
        valid, message = registration_logic.check_username(username)
        return json_success(valid=valid,
                            message=message)

    email = request.args.get("email")
    if email:
        valid, message = registration_logic.check_email(email)
        return json_success(valid=valid, message=message)

    return json_failure(message=error_messages.argument_missing)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.get_by_login_credentials(form.username_or_email.data,
                                             form.password.data)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            message = "Username or password incorrect."
            return message

    return 'Login: %s' % str(form.errors)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
