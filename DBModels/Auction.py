from sqlalchemy import Column, Integer, ForeignKey, DateTime
from DBModels import Base
from datetime import datetime
from DBModels.Item import Item


class Auction(Base):
    __tablename__ = "auctions"

    auctionId = Column(Integer, primary_key=True)
    itemId = Column(Integer, ForeignKey(Item.itemId))
    quantity = Column(Integer)
    buyout = Column(Integer)
    unitPrice = Column(Integer)
    bid = Column(Integer)
    dateInserted = Column(DateTime)
    dirty = Column(Integer)

    def __init__(self, auctionId: int, itemId: int, quantity: int, buyout: int, unitPrice: int, bid: int, dateInserted: datetime):
        self.auctionId = auctionId
        self.itemId = itemId
        self.quantity = quantity
        self.buyout = buyout
        self.unitPrice = unitPrice
        self.bid = bid
        self.dateInserted = dateInserted
        self.dirty = 0

