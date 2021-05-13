from app.models import User
from .forms import LoginForm
from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, request, url_for, flash, Blueprint, make_response

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/', methods=['GET', 'POST'])
def index():
    return "123456"


@auth.route("/wxlogin", methods=['GET', 'POST'])
def wxlogin():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.get(User.username == form.username.data)
            if user.verify_password(form.password.data):
                login_user(user, form.remember.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('用户名或密码错误')
        except:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    login_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))