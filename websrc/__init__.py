import os
from flask import Flask
app = Flask(__name__)
app.secret_key = os.environ["Flask_Key"].encode("utf-8")

from websrc.web import *
