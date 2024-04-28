# import pymongo
# import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func, text
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
        fullname='ian nascimento Souza',
        email_user=[Address(email='iannascimento@gmail.com'), Address(email='ianbrasilcv@gmail.com')]
    )

    bruna = User(
        name='bruna',
        fullname='bruna nascimento Castro',
        email_user=[Address(email='brubru@gmail.com')]
    )

    # send to BD
    session.add_all([iuri, ian, bruna])

    session.commit()


# searching in database
stmt = select(User).where(User.name.in_(["iuri"]))
for user in session.scalars(stmt):
    print(user)

print("\n################ NEXT EXAMPLE ###########################n\n")

# select all user order by name
order_Users = select(User).order_by(User.fullname.asc())
for order in session.scalars(order_Users):
    print(order)

print("\n################ NEXT EXAMPLE ###########################n\n")

# select all users and them e-mails
stmt_join = select(User.fullname, Address.email).join_from(Address, User)
connection = engine.connect()
result = connection.execute(stmt_join).fetchall()
for result_join in result:
    print(result_join)


print("\n################ NEXT EXAMPLE ###########################n\n")
x = 0
stmt_count_users = select(func.count('*')).select_from(User)
for result_count_users in session.scalars(stmt_count_users):
    x = result_count_users

print(f'Total de {x} usuarios cadastrados')


session.close()
