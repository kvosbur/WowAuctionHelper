from sqlalchemy import Column, Integer
from DBModels import Base


class Media(Base):
    __tablename__ = "media"

    mediaId = Column(Integer, primary_key=True)
    mediaURL = Column(Integer, nullable=True)

    def __init__(self, mediaId: int, mediaURL: int):
        self.mediaId = mediaId
        self.mediaURL = mediaURL