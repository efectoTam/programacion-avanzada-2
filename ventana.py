from tkinter import *
from tkinter import ttk

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
titulo = Label(tab1, text="Estos son todos los libros que tenemos en la biblioteca")
titulo.place(x=10, y=10)

# Contenido pestaña 2
titulo = Label(tab2, text="Escribe el nombre del libro")
titulo.place(x=10, y=10)

# Contenido pestaña 3
titulo = Label(tab3, text="Ingresa los datos del libro que quieres donar")
titulo.place(x=10, y=10)

ventanaBiblioteca.mainloop()