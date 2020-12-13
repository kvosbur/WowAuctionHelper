
import os
from flask import Flask
from websrc.constants import login_manager
app = Flask(__name__)
app.secret_key = os.environ["Flask_Key"].encode("utf-8")


login_manager.init_app(app)


from websrc.web import *
from websrc.auction import *
