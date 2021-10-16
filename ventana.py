from tkinter import *
from tkinter import ttk
import pymysql

class Libro:
    def __init__(self, nombre, autor):
        self.nombre=nombre
        self.autor=autor
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca_temuco'
        )
        self.cursor = self.connection.cursor()

    def selectLibros(self):
        sql = "SELECT * from libros"
        try:
            global results
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        
        except Exception as e:
            raise

libro1 = Libro("It", "Stephen King")
libro1.selectLibros()

 # Ventana
ventanaBiblioteca = Tk()
ventanaBiblioteca.title("Biblioteca Temuco")
ventanaBiblioteca.geometry("700x400")

# Pestañas
nb = ttk.Notebook(ventanaBiblioteca)
nb.pack(fill="both", expand="yes")
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
tab3 = ttk.Frame(nb)
nb.add(tab1, text = "Todos los libros")
nb.add(tab2, text = "Búsqueda por nombre")
nb.add(tab3, text = "Donar libro")

# Contenido pestaña 1
titulo = Label(tab1, text=" \n Estos son todos los libros que tenemos en la biblioteca \n \n")
titulo.pack(anchor="w")

for row in results:
    nombre = Label(tab1, text="Nombre: " + row[0])
    autor = Label(tab1, text="Autor: " + row[1])
    descripcion = Label(tab1, text="Descripción: " + row[2])
    publicacion = Label(tab1, text="Año de publicación: " + str(row[3]))
    cantidad = Label(tab1, text="Cantidad: " + str(row[4]))
    colaborador = Label(tab1, text="Nombre colaborador: " + row[5])
    disponibilidad = Label(tab1, text="Disponible: " + row[6])
    tipoPrestamo = Label(tab1, text="Tipo de préstamo: " + row[7])
    diasPrestamo = Label(tab1, text="Días de préstamo: " + str(row[8]) + "\n")
    nombre.pack(anchor="w")
    autor.pack(anchor="w")
    descripcion.pack(anchor="w")
    publicacion.pack(anchor="w")
    cantidad.pack(anchor="w")
    colaborador.pack(anchor="w")
    disponibilidad.pack(anchor="w")
    tipoPrestamo.pack(anchor="w")
    diasPrestamo.pack(anchor="w")


# Contenido pestaña 2
titulo = Label(tab2, text="Escribe el nombre del libro")
titulo.place(x=10, y=10)

# Contenido pestaña 3
titulo = Label(tab3, text="Ingresa los datos del libro que quieres donar")
titulo.place(x=10, y=10)

ventanaBiblioteca.mainloop()