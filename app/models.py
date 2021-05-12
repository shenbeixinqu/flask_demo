from exts import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login_manager
from conf.config import config

import os
import json

cfg = config[os.getenv('FLASK_CONFIG') or 'default']


# 员工表
class User(db.Model, UserMixin):
    __tablename__ = 'mb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    status = db.Column(db.Boolean(default=True))

    def verify_password(self, raw_password):
        return check_password_hash(self.password,raw_password)