from app import db, login_manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(512))

    def __repr__(self):
        return f"<User: {self.email}>"


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))