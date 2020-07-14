from sqlalchemy import Column, Integer, Text, ForeignKey, PrimaryKeyConstraint
from DBModels import Base, ItemClass


class ItemSubClass(Base):
    __tablename__ = "item_subclass"

    subClassId = Column(Integer)
    classId = Column(Integer, ForeignKey(ItemClass.ItemClass.classId))
    name = Column(Text)

    __table_args__ = (
        PrimaryKeyConstraint(subClassId, classId),
        {},
    )

    def __init__(self, subClassId: int, classId: int, name: str):
        self.subClassId = subClassId
        self.classId = classId
        self.name = name



