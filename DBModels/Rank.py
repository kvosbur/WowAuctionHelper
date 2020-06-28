from sqlalchemy import Column, Integer, String, ForeignKey
from DBModels import Base


class Rank(Base):
    __tablename__ = "rank"

    rankId = Column(Integer, primary_key=True)
    recipeId = Column(Integer, ForeignKey("recipe.recipeId"))
    rankValue = Column(Integer)
    quantityMade = Column(Integer)

    def __init__(self, rankId: int, recipeId: int, rankValue: int, quantityMade: int):
        self.rankId = rankId
        self.recipeId = recipeId
        self.rankValue = rankValue
        self.quantityMade = quantityMade
        

