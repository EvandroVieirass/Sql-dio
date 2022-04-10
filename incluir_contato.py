from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos(nome,telefone) VALUES (%s,%s)'
args=('Lucas','995876545')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor ()
        cursor.execute (sql,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'erro: {e.msg}')
    else:
        print ('1 registro incluido ID:',cursor.lastrowid)