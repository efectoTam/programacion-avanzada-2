from tkinter import *
from tkinter import ttk
import pymysql

class Libro:
    def __init__(self):
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

libro1 = Libro()
libro1.selectLibros()

# Ventana
ventanaBiblioteca = Tk()
ventanaBiblioteca.title("Biblioteca Temuco")
w, h = ventanaBiblioteca.winfo_screenwidth(), ventanaBiblioteca.winfo_screenheight()
ventanaBiblioteca.geometry("%dx%d+0+0" % (w, h))

# Pestañas
nb = ttk.Notebook(ventanaBiblioteca)
nb.pack(fill="both", expand="yes")
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
tab3 = ttk.Frame(nb)
nb.add(tab1, text = "Todos los libros")
nb.add(tab2, text = "Búsqueda por nombre")
nb.add(tab3, text = "Donar libro")

# Canvas y scroll
canvas1 = Canvas(tab1)
scroll = Scrollbar(tab1, command=canvas1.yview)
canvas1.config(yscrollcommand=scroll.set, scrollregion=(0,0,0,1550))
canvas1.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)
tabOne = Frame(canvas1)
canvas1.create_window(650, 740, window=tabOne)

# Contenido pestaña 1
titulo = Label(tabOne, text=" \n Estos son todos los libros que tenemos en la biblioteca \n \n")
titulo.pack(anchor="w")

for row in results:
    nombre = Label(tabOne, text="Nombre: " + row[0])
    autor = Label(tabOne, text="Autor: " + row[1])
    descripcion = Label(tabOne, text="Descripción: " + row[2])
    publicacion = Label(tabOne, text="Año de publicación: " + str(row[3]))
    cantidad = Label(tabOne, text="Cantidad: " + str(row[4]))
    colaborador = Label(tabOne, text="Nombre colaborador: " + row[5])
    disponibilidad = Label(tabOne, text="Disponible: " + row[6])
    tipoPrestamo = Label(tabOne, text="Tipo de préstamo: " + row[7])
    diasPrestamo = Label(tabOne, text="Días de préstamo: " + str(row[8]) + "\n")
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