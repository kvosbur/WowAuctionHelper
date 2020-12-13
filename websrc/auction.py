from flask import render_template, session, request, redirect, url_for
from websrc import app
from Database.web import get_user_by_name, register_user, update_data
from flask_login import login_user, login_required, current_user
import hashlib
from datetime import timedelta
import json


@app.route("/auction/login", methods=["GET"])
def auction_login():
    error = request.args.get("error", "")
    return render_template("login.html", Error=error)


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
        return redirect(url_for("auction_login", error="Incorrect Password"))

    if login != "":
        user_obj = get_user_by_name(userName)
        if user_obj is None:
            return redirect(url_for("auction_login", error="User name does NOT exist"))
        login_user(user_obj)
        return redirect(url_for('get_auctions'))

    if register != "":
        user_obj = register_user(userName)
        if user_obj is None:
            return redirect(url_for("auction_login", error="User name already exists"))
        login_user(user_obj)
        return redirect(url_for('get_auctions'))


@app.route('/auction', methods=["GET"])
@login_required
def get_auctions():
    dataObj = json.loads(current_user.data)
    collections = list(dataObj.keys())
    print(current_user.id, current_user.data, current_user.userName)
    if len(collections) > 0:
        collectionName = request.args.get("collectionName") or collections[0]
        collectionDetail = dataObj[collectionName]
        print(collectionDetail)
        return render_template("auction.html", Collections=collections, CollectionDetail=collectionDetail)
    return render_template("auction.html", Collections=collections)


@app.route('/auction/collections', methods=["POST"])
@login_required
def add_collection():
    name = request.form.get("name", "")
    dataObj = json.loads(current_user.data)
    if name != "" and name not in dataObj:
        dataObj[name] = {}
        new_data = json.dumps(dataObj)
        update_data(current_user.get_id(), new_data)
        return redirect(url_for("get_auctions", collectionName=name))

    return redirect(url_for("get_auctions"))


