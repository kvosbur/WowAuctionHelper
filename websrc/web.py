from flask import render_template, session, request, redirect, url_for
from websrc import app


@app.route("/")
def dungeonSuggest():
    try:
        characterName = session["characterName"]
    except Exception:
        characterName = ""

    print(characterName)

    return render_template("dungeon.html", Description="blahblah")


@app.route("/dungeonSubmit", methods=["POST"])
def dungeonSubmit():
    characterName = request.form.get("characterName", "")
    session["characterName"] = characterName
    return redirect(url_for("dungeonSuggest"))