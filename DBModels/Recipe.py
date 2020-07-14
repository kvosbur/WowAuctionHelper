from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base
from DBModels.Item import Item

class Recipe(Base):
    __tablename__ = "recipe"

    recipeId = Column(Integer, primary_key=True)
    profId = Column(Integer, ForeignKey("profession.profId"))
    name = Column(Text)
    minReq = Column(Integer)
    resultItemId = Column(Integer, ForeignKey(Item.itemId))

    def __init__(self, recipeId: int, profId: int, name: str, minReq: int, resultItemId: int):
        self.recipeId = recipeId
        self.profId = profId
        self.name = name
        self.minReq = minReq
        self.resultItemId = resultItemId

