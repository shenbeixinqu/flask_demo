from flask import Blueprint, redirect, url_for, render_template, request
from app import get_logger, get_config
from flask_login import login_required, current_user


logger = get_logger(__name__)
cfg = get_config()

main = Blueprint('main', __name__, url_prefix='/main')


# 根目录跳转
@main.route('/', methods=['GET'])
def root():
    return redirect(url_for('main.index'))


# 首页
@main.route('/index', methods=['GET'])
# @login_required
def index():
    return render_template('index.html', current_user=current_user)

