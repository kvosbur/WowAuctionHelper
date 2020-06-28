from sqlalchemy import Column, Integer, String, ForeignKey
from DBModels import Base


class Item(Base):
    __tablename__ = "item"

    itemId = Column(Integer, primary_key=True)
    classId = Column(Integer, ForeignKey("item_class.classId"))
    subClassId = Column(Integer, ForeignKey("item_class.classId"))
    name = Column(String)
    mediaId = Column(Integer, ForeignKey("media.mediaId"))

    def __init__(self, itemId: int, classId: int, subClassId: int, name: str, mediaId: int):
        self.itemId = itemId
        self.classId = classId
        self.subClassId = subClassId
        self.name = name
        self.mediaId = mediaId
