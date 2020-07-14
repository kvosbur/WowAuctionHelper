from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from DBModels import Base


class EncounterItems(Base):
    __tablename__ = "encounterItems"

    encounterId = Column(Integer, ForeignKey("encounter.encounterId"))
    itemId = Column(Integer, ForeignKey("item.itemId"))
    __table_args__ = (
        PrimaryKeyConstraint('encounterId', 'itemId'),
        {},
    )


    def __init__(self, encounterId, itemId):
        self.encounterId = encounterId
        self.itemId = itemId

