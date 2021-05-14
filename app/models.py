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
    status = db.Column(db.Boolean())

    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


# 员工配置表
class CfgNotify(db.Model):
    check_order = db.Column(db.Integer)  # 排序
    notify_type = db.Column(db.String(100))  # 通知类型
    notify_name = db.Column(db.String(100))  # 通知人姓名
    notify_number = db.Column(db.String(100))  # 通知号码
    status = db.Column(db.Boolean())  # 生效失效标识
