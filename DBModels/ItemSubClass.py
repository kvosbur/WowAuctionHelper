from sqlalchemy import Column, Integer, String, ForeignKey
from DBModels import Base


class ItemSubClass(Base):
    __tablename__ = "item_subclass"

    subClassId = Column(Integer, primary_key=True)
    classId = Column(Integer, ForeignKey("item_class.classId"))
    name = Column(String)

    def __init__(self, subClassId: int, classId: int, name: str):
        self.subClassId = subClassId
        self.classId = classId
        self.name = name



