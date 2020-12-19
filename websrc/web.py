from flask import render_template, session, request, redirect, url_for
from websrc import app
from GatherData import GetItemData
import pickle


#@app.route("/")
def dungeonSuggest():
    try:
        characterObj = pickle.loads(session["characterObject"])
        description = "Please choose your prefrences on items to be chosen."
    except Exception:
        description = "Please enter in your character name in order to begin."

    return render_template("dungeon.html", Description=description)


#@app.route("/dungeonSubmit", methods=["POST"])
def dungeonSubmit():
    characterName = request.form.get("characterName", "")
    characterObj = None
    if characterName != "":
        characterObj = GetItemData.get_equipment_for_character(characterName)
    session["characterObject"] = pickle.dumps(characterObj)
    return redirect(url_for("dungeonSuggest"))