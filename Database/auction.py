from Database import session
import datetime
from DBModels.Auction import Auction
from Database.item import addItemById
from Models.auction import GetAuction

def auction_exists(auctionId):
    if session.query(Auction).filter(Auction.auctionId == auctionId).first() is not None:
        return True
    return False


def add_all_auctions(auctions: GetAuction):
    count = 0
    print(len(auctions.auctions))
    auctions.auctions.sort(key=lambda auc: auc.item.id)
    current_item = auctions.auctions[0].item.id
    for auction in auctions.auctions:
        if auction_exists(auction.id):
            continue
        count += 1
        item_id = auction.item.id
        if item_id != current_item:
            addItemById(item_id)
            current_item = item_id

        obj = Auction(auction.id, item_id, auction.quantity, auction.buyout, auction.unit_price,
                              auction.bid, datetime.datetime.now())
        session.add(obj)
    session.commit()
    print(count)


