from DBModels import Base

import sqlalchemy

from sqlalchemy.orm import sessionmaker
import os

db_user = os.environ["DB_User"]
db_password = os.environ["DB_Password"]

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://{}:{}@localhost:3306/wow_auction'.format(db_user, db_password))


for tbl in reversed(Base.metadata.sorted_tables):
    engine.execute(tbl.delete())




Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

