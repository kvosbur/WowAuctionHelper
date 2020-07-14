from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base
from DBModels.Dungeon import Dungeon

class Encounter(Base):
    __tablename__ = "encounter"

    encounterId = Column(Integer, primary_key=True, autoincrement=False)
    journDungId = Column(Integer, ForeignKey(Dungeon.journDungId))
    name = Column(Text)

    def __init__(self, encounterId, journDungId, name):
        self.encounterId = encounterId
        self.journDungId = journDungId
        self.name = name

