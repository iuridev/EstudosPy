import pprint
import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'bd_studying.db')

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def create_table(conexao, cursor, table):
    table_name = table
    cursor.execute(
        'CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))', table_name)
    conexao.commit()


def insert_user(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', data)
    conexao.commit()


def insert_many_user(conexao, cursor, lis):
    data = lis
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', data)
    conexao.commit()


def update_user(conexao, cursor, nome, email, idd):
    data = (nome, email, idd)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?', data)
    conexao.commit()


def select_user(cursor, idd):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (idd,))
    result = cursor.fetchone()
    pprint.pprint(dict(result))


def select_users(cursor):
    cursor.execute('SELECT * FROM clientes ORDER BY nome')
    result = cursor.fetchall()
    for rows in result:
        pprint.pprint(dict(rows))


# update_user(conexao, cursor, 'Iuri', 'iuribarreto@gmail.com', 1)

lis = [('marcos', 'marcos@hotmail.com'), ('yasmim',
                                          'yasmim@yahoo.com'), ('cleber', 'cleber@gmail.com')]

# insert_many_user(conexao, cursor, lis)

select_user(cursor, 1)
select_users(cursor)
