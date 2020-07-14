from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base, PlayerClassSpecialization


class AzeriteTrait(Base):
    __tablename__ = "azerite_trait"

    spell_id = Column(Integer, primary_key=True, autoincrement=False)
    tier = Column(Integer)
    name = Column(Text)
    playerClassSpecId = Column(Integer, ForeignKey(PlayerClassSpecialization.PlayerClassSpecialization.playerClassSpecId))

    def __init__(self, spell_id: int, tier: int, name: str, playerClassSpecId: int):
        self.spell_id = spell_id
        self.tier = tier
        self.name = name
        self.playerClassSpecId = playerClassSpecId



