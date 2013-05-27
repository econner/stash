from flask import g
from flask.ext.login import current_user
from flask.ext.login import LoginManager

from app import app
from models.user_model import User

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(pk=unicode(user_id))
    except User.DoesNotExist:
        return None


@app.before_request
def before_request():
    # make the current user global to the request
    g.user = current_user
