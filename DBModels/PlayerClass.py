from sqlalchemy import Column, Integer, Text
from DBModels import Base


class PlayerClass(Base):
    __tablename__ = "player_class"

    playerClassId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(Text)

    def __init__(self, playerClassId: int, name: str):
        self.playerClassId = playerClassId
        self.name = name



