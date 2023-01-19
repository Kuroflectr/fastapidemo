from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api_v2.db import Base


class Movie(Base):
    __tablename__ = "MOVIES_S"

    movieid = Column(Integer, primary_key=True)
    title = Column(String(1024))
    genres = Column(String(1024))
