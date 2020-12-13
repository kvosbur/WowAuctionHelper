from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, userId, userName, userData):
        super().__init__()
        self.data = userData
        self.id = userId
        self.userName = userName

    def get_id(self):
        return self.id