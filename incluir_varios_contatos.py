from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos(nome,telefone) VALUES (%s,%s)'
args=(
    ('lia','9865622546')
    ('lu','58965324785')
    ('joão','62478956339')
    ('pedro','9865633365')
    ('roberto','78549888562')
    ('carlos','54879565899')
    ('maria','99002214789')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor ()
        cursor.executemany (sql,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'erro: {e.msg}')
    else:
        print (f'{cursor.rowcount} registros incluidos ID')