import sqlite3

print('Entrando no arquivo de execução do banco!')

try:
    conn = sqlite3.connect('gian.sqlite3')
    print('Você está conectado!')
except Exception:
    print('Sua conexão falhou, verifique novamente!')

if conn is not None:
    print('Conexão estabilazada...')

    cursor = conn.cursor()

    cursor.execute('CREATE TABLE pessoa (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(15) NOT NULL, idade INTEGER NOT NULL, altura VARCHAR(20) NOT NULL);')
    print('Sua tabela pessoa foi criada!')

    cursor.execute('CREATE TABLE usuarios (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30) PRIMARY KEY NOT NULL, senha VARCHAR(30) NOT NULL);')
    print('Sua tabela usuarios foi criada!')

    conn.commit()
    cursor.close()
    conn.close()