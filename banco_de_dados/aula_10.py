# import pymongo
# import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# first pass is to create a Base
Base = declarative_base()


class User(Base):
    __table_name__ = "user_account"  # create table

    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)

    # relation ForeignKey
    email_user = relationship(
        "Address", back_populates="user", cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"User( id: {self.id}, name: {self.name}, fullname: {self.fullname} )"


class Address(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    # relation ForeignKey
    user = relationship(
        "User", back_populates="email_user"
    )

    def __repr__(self):
        return f"Address( id: {self.id}, Email: {self.email})"
