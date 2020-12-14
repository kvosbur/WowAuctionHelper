from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base, ItemClass, ItemSubClass

Stats = {"INTELLECT": "intellect", "STAMINA": "stamina", "AGILITY": "agility", "STRENGTH": "strength",
         "CRIT_RATING": "critStrike", "MASTERY_RATING": "master", "HASTE_RATING": "haste", "VERSATILITY": "versatility"}


class Item(Base):
    __tablename__ = "item"

    itemId = Column(Integer, primary_key=True, autoincrement=False)
    classId = Column(Integer, ForeignKey(ItemClass.ItemClass.classId))
    subClassId = Column(Integer, ForeignKey(ItemSubClass.ItemSubClass.subClassId))
    name = Column(Text)
    inventoryType = Column(Text)
    mediaId = Column(Integer, ForeignKey("media.mediaId"))
    vendorPrice = Column(Integer)

    # stat columns (boolean on if present since scaled with lvl)
    # primary stats
    intellect = Column(Integer)
    agility = Column(Integer)
    strength = Column(Integer)
    stamina = Column(Integer)

    # secondary stats
    critStrike = Column(Integer)
    haste = Column(Integer)
    mastery = Column(Integer)
    versatility = Column(Integer)

    def __init__(self, itemId: int, classId: int, subClassId: int, name: str, mediaId: int, inventoryType: str,
                 vendorPrice: int = 0, intellect: int = 0, agility: int = 0, strength: int = 0, stamina: int = 0,
                 critStrike: int = 0, haste: int = 0, master: int = 0, versatility: int = 0):
        self.itemId = itemId
        self.classId = classId
        self.subClassId = subClassId
        self.name = name
        self.mediaId = mediaId
        self.inventoryType = inventoryType
        self.vendorPrice = vendorPrice
        self.intellect = intellect
        self.agility = agility
        self.strength = strength
        self.stamina = stamina
        self.critStrike = critStrike
        self.haste = haste
        self.master = master
        self.versatility = versatility
