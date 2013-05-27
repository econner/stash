from core.logic import auth_logic
from app import db


class User(db.Document):
    email = db.StringField(required=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.pk)

    @classmethod
    def get_by_login_credentials(cls, username_or_email, password):
        """Get a user matching the specified credentials or None."""
        user = cls.objects.get(username=username_or_email)
        if not user:
            user = cls.objects(email=username_or_email)

        if user and auth_logic.check_password(password, user.password):
            return user

        return None

    def __repr__(self):
        return "User<%s>" % self.username
