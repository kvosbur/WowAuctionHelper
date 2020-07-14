from sqlalchemy import Column, Integer, Text, PrimaryKeyConstraint
from DBModels import Base


class Dungeon(Base):
    __tablename__ = "dungeon"

    journDungId = Column(Integer)
    mythDungId = Column(Integer)
    name = Column(Text)
    __table_args__ = (
        PrimaryKeyConstraint(journDungId, mythDungId),
        {},
    )

    def __init__(self, mythDungId, journDungId, name):
        self.mythDungId = mythDungId
        self.journDungId = journDungId
        self.name = name

