from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base, PlayerClassSpecialization, PlayerClass


class AzeriteTrait(Base):
    __tablename__ = "azerite_trait"

    power_id = Column(Integer, primary_key=True, autoincrement=False)
    tier = Column(Integer)
    name = Column(Text)
    playerClassId = Column(Integer,
                               ForeignKey(PlayerClass.PlayerClass.playerClassId))

    def __init__(self, power_id: int, tier: int, name: str, playerClassId: int):
        self.power_id = power_id
        self.tier = tier
        self.name = name
        self.playerClassId = playerClassId



