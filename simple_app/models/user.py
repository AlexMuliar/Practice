import sys
import os
import random
import string

from config import db



def generate_string(N=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


class User(db.Model):
    __tablename__ = 'users'

    id_ = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    birthday = db.Column(db.Date(), nullable=True)
    inactive = db.Column(db.Boolean(), default=True)


    @staticmethod
    def create_random_user() -> None:
        user = User()
        user.name = generate_string()
        user.last_name = generate_string(8)
        user.password = generate_string(8)
        db.session.add(user)
        db.session.commit()
        return user


if __name__ == '__main__':
    db.create_all()