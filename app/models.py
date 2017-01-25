from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class user(db.Model):
    id