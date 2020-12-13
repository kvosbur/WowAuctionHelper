from Database import session
from DBModels.WebUser import WebUser
from websrc.user import User
import uuid


def get_user_by_name(user_name):
    userObj = session.query(WebUser).filter(WebUser.userName == user_name).first()
    if userObj is not None:
        return User(userObj.userId, userObj.userName, userObj.data)
    return None


def get_user_by_id(user_id):
    userObj = session.query(WebUser).filter(WebUser.userId == user_id).first()
    if userObj is not None:
        return User(userObj.userId, userObj.userName, userObj.data)
    return None


def register_user(user_name):
    if get_user_by_name(user_name):
        return None
    obj = WebUser(uuid.uuid4().hex, user_name, '{}')
    session.add(obj)
    session.commit()
    return User(obj.userId, obj.userName, obj.data)


def update_data(user_id, new_data):
    session.query(WebUser).filter(WebUser.userId == user_id).update({WebUser.data: new_data})
    session.commit()
