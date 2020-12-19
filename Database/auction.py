from Database import session
import datetime
from sqlalchemy import or_, func
from DBModels.Auction import Auction
from Database.item import addItemById, get_item_by_name
from Models.auction import GetAuction


def auction_exists(auctionId):
    return session.execute('select auctionId from auctions where auctionId = :val',
                           {'val': auctionId}).first() is not None


def insert_or_update_auc(auction):
    session.execute('''
    INSERT INTO auctions (auctionId, itemId, quantity, buyout, unitPrice, bid, dateInserted, dirty)
    VALUES (:id, :itemId, :quantity, :buyout, :unitPrice, :bid, :dateInserted, :dirty)
    ON DUPLICATE KEY UPDATE
        quantity = :quantity,
        bid = :bid,
        dirty = :dirty
    ''', {'id': auction.id,
          'itemId': auction.item.id,
          'quantity': auction.quantity,
          'buyout': auction.buyout,
          'unitPrice': auction.unit_price,
          'bid': auction.bid,
          'dateInserted': datetime.datetime.now(),
          'dirty': 0})


def add_all_auctions(auctions: GetAuction):
    print(len(auctions.auctions))
    auctions.auctions.sort(key=lambda auc: auc.item.id)
    set_auctions_dirty()
    current_item = auctions.auctions[0].item.id
    addItemById(current_item)
    count = 0
    for auction in auctions.auctions:
        count += 1
        if count % 2000 == 0 and count != 0:
            print("Amount Processed:", count)

        item_id = auction.item.id
        if item_id != current_item:
            resp = addItemById(item_id)
            if resp is None:
                continue
            current_item = item_id

        insert_or_update_auc(auction)
        session.commit()

    remove_dirty_auctions()
    session.commit()
    print(count)


def clean_auction(auction_id, new_quantity):
    session.query(Auction).filter(Auction.auctionId == auction_id).update(
        {Auction.dirty: 0, Auction.quantity: new_quantity})
    session.commit()


def set_auctions_dirty():
    session.query(Auction).filter(Auction.dirty == 0).update({Auction.dirty: 1})
    session.commit()


def remove_dirty_auctions():
    session.query(Auction).filter(Auction.dirty == 1).update({Auction.dateRemoved: datetime.datetime.now()})
    session.commit()


def get_auction_data(items, amount_return):
    data = {}
    for item in items:
        itemObj = get_item_by_name(item)
        auctions = session.query(Auction.unitPrice, Auction.buyout, func.sum(Auction.quantity)) \
            .group_by(Auction.unitPrice, Auction.buyout) \
            .filter(Auction.itemId == itemObj.itemId, or_(Auction.buyout != None, Auction.unitPrice != None)) \
            .order_by(Auction.unitPrice.asc()).limit(amount_return).all()
        data[item] = auctions
    return data


def get_most_recently_added_date():
    return session.query(Auction.dateInserted).order_by(Auction.dateInserted.desc()).first()
