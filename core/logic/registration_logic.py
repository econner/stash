from core.logic import auth_logic
from models.user_model import User
from utils.validation_utils import validate_email
from messages import error_messages


def check_username(username):
    if len(username) < 4:
        return False, error_messages.value_too_short

    username_taken = len(User.objects(username=username)) > 0
    if username_taken:
        return False, error_messages.username_taken

    return True, None


def check_email(email):
    if len(email) < 6:
        return False, error_messages.value_too_short

    email_valid = validate_email(email)
    if not email_valid:
        return False, error_messages.email_invalid

    email_exists = len(User.objects(email=email)) > 0
    if email_exists:
        return False, error_messages.email_taken

    return True, None


def register_user(form):
    encoded_pw = form.password.data.encode('utf-8')
    hashed_password = auth_logic.hash_password(encoded_pw)
    user = User(username=form.username.data,
                email=form.email.data,
                password=hashed_password)
    user.save()
    return unicode(user.pk)
