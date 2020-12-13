from flask import render_template, session, request, redirect, url_for
from websrc import app
from Database.web import get_user_by_name, register_user
from flask_login import login_user
import hashlib
from datetime import timedelta


@app.route("/auction/login", methods=["GET"])
def auction_login():
    return render_template("login.html")


@app.route("/auction/user", methods=["POST"])
def do_auction_login():
    password = request.form.get("password", "")
    login = request.form.get("login", "")
    register = request.form.get("register", "")
    userName = request.form.get("userName", "")

    m = hashlib.sha512()
    m.update(password.encode('utf-8'))
    digest = m.digest()
    if digest != b"\x1b\xf2\xb4\x1do\x86\xe4o\x7f\xe8\x0e\x161\xba[\xf6\xdc&/\xc84\xb9uo` \x95\t#\x00\xa1\x99\x80\x8c\xa5w\xc0E8'%\xa1\xa0\xfe[\x94^\xa6%\xe3,l@\xa1\xe6~m\xc6\xba\xf9\xe9\xc2\xa51":
        return redirect(url_for("auction_login"))

    if login != "":

        login_user(get_user_by_name(userName))
        return 'logged in'

    if register != "":
        user_obj = register_user(userName)
        login_user(user_obj, remember=True, duration=timedelta(days=720))
        return 'register'



