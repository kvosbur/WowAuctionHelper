from sqlalchemy import Column, VARCHAR, Text
from DBModels import Base


class WebUser(Base):
    __tablename__ = "webuser"

    userId = Column(VARCHAR(length=36), primary_key=True)
    userName = Column(VARCHAR(length=50))
    data = Column(Text)

    def __init__(self, userId: str, userName: str, data: str):
        self.userId = userId
        self.userName = userName
        self.data = data


