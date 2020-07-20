from sqlalchemy import Column, Integer, Text, ForeignKey, PrimaryKeyConstraint
from DBModels import Base, Item, AzeriteTrait


class AzeriteItem(Base):
    __tablename__ = "azerite_item"

    itemId = Column(Integer, ForeignKey(Item.Item.itemId))
    power_id = Column(Integer, ForeignKey(AzeriteTrait.AzeriteTrait.power_id))

    __table_args__ = (
        PrimaryKeyConstraint(itemId, power_id),
        {},
    )

    def __init__(self, itemId: int, power_id: int):
        self.itemId = itemId
        self.power_id = power_id



