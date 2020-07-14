from sqlalchemy import Column, Integer, Text
from DBModels import Base


class Media(Base):
    __tablename__ = "media"

    mediaId = Column(Integer, primary_key=True)
    mediaURL = Column(Text, nullable=True)

    def __init__(self, mediaId: int, mediaURL: str):
        self.mediaId = mediaId
        self.mediaURL = mediaURL