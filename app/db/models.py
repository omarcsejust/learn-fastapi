from ..db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime, BLOB
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    image = Column(BLOB, nullable=True, default=None)




