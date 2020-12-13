from Database.web import get_user_by_id
from flask_login import LoginManager

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)
