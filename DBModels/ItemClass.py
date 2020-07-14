from sqlalchemy import Column, Integer, Text
from DBModels import Base

class ItemClass(Base):
    __tablename__ = "item_class"

    classId = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(Text)

    def __init__(self, classId: int, name: str):
        self.classId = classId
        self.name = name



