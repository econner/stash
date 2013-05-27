import bcrypt


def hash_password(raw_password):
    raw_password = raw_password.encode('utf-8')
    hashed_pw = bcrypt.hashpw(raw_password, bcrypt.gensalt())
    return hashed_pw


def check_password(password, hashed_password):
    password = password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    return bcrypt.hashpw(password, hashed_password) == hashed_password
