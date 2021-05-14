from flask import Flask
from flask_login import LoginManager
from conf.config import config
import logging
from logging.config import fileConfig
from exts import db
import os


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'auth.login'
fileConfig('conf/log-app.conf')


def get_logger(name):
    return logging.getLogger(name)


def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))


def get_config():
    return config[os.getenv('FLASK_CONFIG') or 'default']


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 如果出现 Missing user_loader or request_loader 添加下面三行
    @login_manager.user_loader
    def load_user(user_id):
        return None

    from app.main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth.views import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
