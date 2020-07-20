from sqlalchemy import Column, Integer, Text, ForeignKey, PrimaryKeyConstraint
from DBModels import Base, PlayerClassSpecialization, AzeriteTrait


class AzeriteClassSpecialization(Base):
    __tablename__ = "azerite_class_spec"

    playerClassSpecId = Column(Integer, ForeignKey(PlayerClassSpecialization.PlayerClassSpecialization.playerClassSpecId))
    power_id = Column(Integer, ForeignKey(AzeriteTrait.AzeriteTrait.power_id))

    __table_args__ = (
        PrimaryKeyConstraint(playerClassSpecId, power_id),
        {},
    )

    def __init__(self, playerClassSpecId: int, power_id: int):
        self.playerClassSpecId = playerClassSpecId
        self.power_id = power_id



