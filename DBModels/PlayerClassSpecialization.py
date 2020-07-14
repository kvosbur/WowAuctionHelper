from sqlalchemy import Column, Integer, Text, ForeignKey, PrimaryKeyConstraint
from DBModels import Base, PlayerClass


class PlayerClassSpecialization(Base):
    __tablename__ = "player_class_spec"

    playerClassSpecId = Column(Integer)
    playerClassId = Column(Integer, ForeignKey(PlayerClass.PlayerClass.playerClassId))
    name = Column(Text)

    __table_args__ = (
        PrimaryKeyConstraint(playerClassSpecId, playerClassId),
        {},
    )

    def __init__(self, playerClassSpecId: int, playerClassId: int, name: str):
        self.playerClassSpecId = playerClassSpecId
        self.playerClassId = playerClassId
        self.name = name



