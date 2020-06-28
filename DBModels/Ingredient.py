from sqlalchemy import Column, Integer, String, ForeignKey
from DBModels import Base


class Ingredient(Base):
    __tablename__ = "ingredient"

    ingredientId = Column(Integer, primary_key=True)
    rankId = Column(Integer, ForeignKey("rank.rankId"))
    itemId = Column(Integer, ForeignKey("item.itemId"))
    quantity = Column(Integer)

    def __init__(self, ingredientId: int, rankId: int, itemId: int, quantity: int):
        self.ingredientId = ingredientId
        self.rankId = rankId
        self.itemId = itemId
        self.quantity = quantity


