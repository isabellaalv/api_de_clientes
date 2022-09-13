# import sqlalchemy
#
#
# def conexao():
#     server = 'localhost'
#     database = 'cliente'
#     username = 'sa'
#     DRIVER = 'SQL+Server+Native+Client+10.0'
#     password = 'alves'
#     DATABASE_CONNECTION = (f"DRIVER={DRIVER};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#
#     engine = sqlalchemy.create_engine(DATABASE_CONNECTION)
#     conecta = engine.connect()
#
#     return conecta


from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def conexao():
    server = 'localhost'
    database = 'cliente'
    username = 'sa'
    password = 'alves'
    driver = 'SQL Server Native Client 10.0'


    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

    engine = create_engine(connection_url)

    return engine


