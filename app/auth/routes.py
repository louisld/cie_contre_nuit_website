import flask
from flask import (
    render_template,
    redirect,
    url_for
)

from flask_login import (
    login_user,
    logout_user,
    current_user
)

from ..auth import auth
from app.auth.models import User
from app.auth.forms import LoginForm
from app.extensions import sitemap

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user: User | None = User.query.filter_by(username=login_form.username.data).first()
        if user is None or user.check_password(login_form.password.data):
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for("admin.dashboard"))
    return render_template(
        "login.html.j2",
        login_form=login_form
    )

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))