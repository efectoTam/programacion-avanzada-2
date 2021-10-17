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

    def CreateDB(self):
        sql = 'CREATE DATABASE biblioteca_temuco'
        try:
            self.cursor.execute(sql)
        except Exception as e:
            raise
    
    def CreateTables(self):
        sql1 = "CREATE TABLE libros(nombre varchar(100), autor varchar(100), descripcion varchar(500), añoPublicacion int, cantidad int, nombreColaborador varchar(100), Disponible varchar(2), tipoPrestamo varchar(15), diasPrestamo int)"
        sql2 = "CREATE TABLE donaciones(nombreLibro varchar(100), autor varchar(100),añoPublicacion int, nombreColaborador varchar(100))"
        try:
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
        except Exception as e:
            raise

    def InsertDataLibros(self, nombre, autor, descripcion, añoPublicacion, cantidad, nombreColaborador, Disponible, tipoPrestamo, diasPrestamo):
        sql = "INSERT INTO libros(nombre, autor, descripcion, añoPublicacion, cantidad, nombreColaborador, Disponible, tipoPrestamo, diasPrestamo) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nombre, autor, descripcion, añoPublicacion, cantidad, nombreColaborador, Disponible, tipoPrestamo, diasPrestamo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


    def close(self):
        self.connection.close()

bibliotecaTemuco = Biblioteca()
bibliotecaTemuco.CreateDB()
bibliotecaTemuco.CreateTables()
bibliotecaTemuco.InsertDataLibros('El relato del monstruo', 'Shaun Hamill', 'No rechazo las decisiones que he tomado ni el precio que he pagado por ellas. Supongo que no resulta tan sorprendente. Mi traje de monstruo siempre me quedó mejor que mi propia piel.', 2020, 2, 'Andrés Silva', 'Si', 'Interno/Externo', '15')
bibliotecaTemuco.InsertDataLibros('Expediente Flisflisher', 'Nekane Flisflisher', '¿Sabías que la escalofriante criatura que inspiró la película The Ring tiene su origen en una leyenda japonesa quegira en torno al castillo de Himeji?¿Y que la caja Dybbuk existe realmente y se encuentra en un museo en Las Vegas?', 2020, 4, 'Roxana Riquelme', 'No', 'Solo externo', '15')
bibliotecaTemuco.InsertDataLibros('La Ciudad sin Nombre', 'H.P. Lovecraft', 'En lo profundo del desierto de Arabia, un explorador está a punto de descubrir la ubicación de la Ciudad Sin Nombre. Pero su entusiasmo es equiparable a su miedo ante la proximidad de este famoso lugar maldito.', 2021, 5, 'Jaime Donoso', 'Si', 'Interno/Externo', '15')
bibliotecaTemuco.InsertDataLibros('Coquimbo Zombi', 'Rodrigo Muñoz', 'El verano de 1986 llega a su fin en el puerto de Coquimbo, es la última noche de febrero y antes de tener que volver al colegio, un grupo de amigos, Valentina, Aníbal, Ignacio y Mauricio, deciden tener una última aventura.', 2021, 3, 'Alejandro Navarrete', 'Si', 'Interno/Externo', '15')
bibliotecaTemuco.InsertDataLibros('Cuentos imprescindibles', 'Edgar Allan Poe', 'Los cuentos de Edgar Allan Poe fueron desde su publicación un hito y un referente inexcusables en la literatura fantástica, de misterio y de terror.', 2019, 1, 'Ximena Aroyo', 'Si', 'Solo interno', '1')
bibliotecaTemuco.InsertDataLibros('Hombre Lobo', 'Lorraine Warren', 'Los relatos auténticos de los demonólogos en los que se inspiraron las películas de Expediente Warren.La leyenda del hombre lobo es tan antigua como la propia humanidad.', 2021, 1, 'Ximena Aroyo', 'Si', 'Solo interno', '1')
bibliotecaTemuco.InsertDataLibros('El Misterio De Salems Lot', 'Stephen King', 'Salems Lot es un pueblo tranquilo donde nunca pasa nada. O quizás esto son solo apariencias, pues lo cierto es que sí se están sucediendo diversos hechos misteriosos, incluso escalofriantes.', 2018, 5, 'Leandro Arancibia', 'Si', 'Interno/Externo', '15')
bibliotecaTemuco.close()