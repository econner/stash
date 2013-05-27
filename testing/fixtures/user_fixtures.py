from core.logic import auth_logic
from models.user_model import User


def factory(username="eric",
            email="eric@example.com",
            password="abc123"):
    hashed_pw = auth_logic.hash_password(password)
    user = User(username=username, email=email, password=hashed_pw)
    user.save()
    return user
