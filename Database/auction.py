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
    addItemById(current_item)
    count = 0
    for auction in auctions.auctions:
        if count % 2000 == 0:
            print("Amount Processed:", count)
        if auction_exists(auction.id):
            clean_auction(auction.id, auction.quantity)
            continue
        item_id = auction.item.id
        if item_id != current_item:
            resp = addItemById(item_id)
            if resp is None:
                continue
            current_item = item_id

        obj = Auction(auction.id, item_id, auction.quantity, auction.buyout, auction.unit_price,
                              auction.bid, datetime.datetime.now())
        session.add(obj)
        session.commit()
        count += 1

    remove_dirty_auctions()
    session.commit()
    print(count)


def clean_auction(auction_id, new_quantity):
    session.query(Auction).filter(Auction.auctionId == auction_id).update({ Auction.dirty: 0, Auction.quantity: new_quantity })
    session.commit()


def set_auctions_dirty():
    session.query(Auction).filter(Auction.dirty == 0).update({ Auction.dirty: 1 })
    session.commit()


def remove_dirty_auctions():
    session.query(Auction).filter(Auction.dirty == 1).update({ Auction.dateRemoved: datetime.datetime.now() })
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

