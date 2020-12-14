from Database import session
import datetime
from sqlalchemy import or_, func
from DBModels.Auction import Auction
from Database.item import addItemById, get_item_by_name
from Models.auction import GetAuction

def auction_exists(auctionId):
    if session.query(Auction).filter(Auction.auctionId == auctionId).first() is not None:
        return True
    return False


def add_all_auctions(auctions: GetAuction):
    count = 0
    print(len(auctions.auctions))
    auctions.auctions.sort(key=lambda auc: auc.item.id)
    set_auctions_dirty()
    current_item = auctions.auctions[0].item.id
    for auction in auctions.auctions:
        if auction_exists(auction.id):
            clean_auction(auction.id)
            continue
        count += 1
        if count % 1000 == 0:
            print(count)
        item_id = auction.item.id
        if item_id != current_item:
            resp = addItemById(item_id)
            if resp is None:
                continue
            current_item = item_id

        obj = Auction(auction.id, item_id, auction.quantity, auction.buyout, auction.unit_price,
                              auction.bid, datetime.datetime.now())
        session.add(obj)

    remove_dirty_auctions()
    session.commit()
    print(count)


def clean_auction(auction_id):
    session.query(Auction).filter(Auction.auctionId == auction_id).update({ Auction.dirty: 0 })
    session.commit()


def set_auctions_dirty():
    session.query(Auction).update({ Auction.dirty: 1 })
    session.commit()


def remove_dirty_auctions():
    session.query(Auction).filter(Auction.dirty == 1).delete()
    session.commit()


def get_auction_data(items, amount_return):
    data = {}
    for item in items:
        itemObj = get_item_by_name(item)
        auctions = session.query(Auction.unitPrice, Auction.buyout, func.sum(Auction.quantity))\
            .group_by(Auction.unitPrice, Auction.buyout)\
            .filter(Auction.itemId == itemObj.itemId, or_(Auction.buyout != None, Auction.unitPrice != None))\
            .order_by(Auction.unitPrice.asc()).limit(amount_return).all()
        data[item] = auctions
    return data


def get_most_recently_added_date():
    return session.query(Auction.dateInserted).order_by(Auction.dateInserted.desc()).first()

