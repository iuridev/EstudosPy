# import pymongo
# import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select
from sqlalchemy.orm import declarative_base, relationship, Session

# first pass is to create a Base
Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    # relation ForeignKey
    email_user = relationship(
        "Address", back_populates="user", cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"User( id: {self.id}, name: {self.name}, fullname: {self.fullname} )"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    # relation ForeignKey
    user = relationship(
        "User", back_populates="email_user"
    )

    def __repr__(self):
        return f"Address( id: {self.id}, Email: {self.email})"


# CONEXÃO COM BANCO DE DADOS : SQLITE
engine = create_engine("sqlite://")

# CRIANDO AS TABELAS NO BANCO DE DADOS - USANDO AS CLASSES QUE CRIAMOS ANTERIOMENTE
Base.metadata.create_all(engine)

inspect_engine = inspect(engine)

print(inspect_engine.get_table_names())

print(inspect_engine.default_schema_name)

# criar sessão para pesistir dados no SQLite
with Session(engine) as session:
    iuri = User(
        name='iuri',
        fullname='iuri santos barreto',
        email_user=[Address(email='iuribarreto.ib@gmail.com')]
    )

    ian = User(
        name='ian',
        fullname='Ian nascimento Souza',
        email_user=[Address(email='iannascimento@gmail.com'), Address(email='ianbrasilcv@gmail.com')]
    )

    # envindo para o BD
    session.add_all([iuri, ian])

    session.commit()

stmt = select(User).where(User.name.in_(["iuri"]))
for user in session.scalars(stmt):
    print(user)
