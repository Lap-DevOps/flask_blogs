from flask import Blueprint, request, redirect, url_for, flash, render_template, session

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


def login_admin():
    session["admin_ligged"] = 1


@admin.route("/")
def index():
    return "admin"


def isLogged():
    return True if session.get("admin_lagged") else False


def logout_admin():
    session.pop('admin_logged', None)


@admin.route('/logout', methods=["POST", "GET"])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))
    logout_admin()

    return redirect(url_for('.login'))


@admin.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin' and request.form['123']:
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash('Not correct login/password')
    return render_template('admin/login.html', title='Admin panel')
