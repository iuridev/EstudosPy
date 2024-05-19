import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'bd_studying.db')

cursor = conexao.cursor()

data = ('maria', 'mariasantos223@gmail.com')
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', data)
conexao.commit()
