from sqlalchemy import Column, Integer, Text, ForeignKey
from DBModels import Base


class Profession(Base):
    __tablename__ = "profession"

    profId = Column(Integer, primary_key=True)
    name = Column(Text)
    # note that as of now bfa will have a value of 0, shadowlands 1
    expansion = Column(Integer)

    def __init__(self, profId: int, name: str, expansion: int):
        self.profId = profId
        self.name = name
        self.expansion = expansion
