from sqlalchemy import Column, Integer, String
from DBModels import Base


class ItemClass(Base):
    __tablename__ = "item_class"

    classId = Column(Integer, primary_key=True)
    parentClassId = Column(Integer, nullable=True)
    name = Column(String)

    def __init__(self, classId: int, parentClassId: int, name: str):
        self.classId = classId
        self.parentClassId = parentClassId
        self.name = name



