import pymysql

class Biblioteca:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca_temuco'
        )
        self.cursor = self.connection.cursor()

    # def CreateDB(self):
    #     sql = 'CREATE DATABASE biblioteca_temuco'
    #     try:
    #         self.cursor.execute(sql)
    #     except Exception as e:
    #         raise
    
    # def CreateTables(self):
    #     sql1 = "CREATE TABLE libros(nombre varchar(100), autor varchar(100), descripcion varchar(500), añoPublicacion int, cantidad int, nombreColaborador varchar(100), Disponible varchar(2), tipoPrestamo varchar(15), diasPrestamo int)"
    #     sql2 = "CREATE TABLE donaciones(nombreLibro varchar(100), autor varchar(100),añoPublicacion int, nombreColaborador varchar(100))"
    #     try:
    #         self.cursor.execute(sql1)
    #         self.cursor.execute(sql2)
    #     except Exception as e:
    #         raise

    def close(self):
        self.connection.close()

bibliotecaTemuco = Biblioteca()
# bibliotecaTemuco.CreateDB()
# bibliotecaTemuco.CreateTables()
bibliotecaTemuco.close()