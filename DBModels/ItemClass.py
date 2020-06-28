from sqlalchemy import Column, Integer, String
from DBModels import Base


class ItemClass(Base):
    __tablename__ = "item_class"

    classId = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, classId: int, name: str):
        self.classId = classId
        self.name = name



