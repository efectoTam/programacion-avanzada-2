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

    # Devuelve todos los libros
    def selectLibros(self):
        sql = "SELECT * from libros"
        try:
            global results
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        
        except Exception as e:
            raise

    # Método cuando se hace clic en Buscar
    def buscarPorNombre(self):
        nombreIngresado = inputNombre.get()
        if nombreIngresado == '':
            inputVacio = Label(tab2, text="Escribe el nombre de un libro antes de buscar")
            inputVacio.pack(anchor="w")
        else: 
            sql = "SELECT nombre, autor, cantidad, Disponible, tipoPrestamo, diasPrestamo FROM libros WHERE nombre = '{}'".format(nombreIngresado)
            try:
                self.cursor.execute(sql)
                specificData = self.cursor.fetchall()
                if specificData == ():
                    sinResultados = Label(tab2, text="\nNo hay resultados para: " + nombreIngresado)
                    sinResultados.pack(anchor="w")
                else:
                    for row in specificData:
                        subtitleResultado = Label(tab2, text="\n\nResultado de la búsqueda")
                        subtitleResultado.pack(anchor="w")
                        specificNombre = Label(tab2, text="Nombre: " + row[0])
                        specificAutor = Label(tab2, text="Autor: " + row[1])
                        specificCantidad = Label(tab2, text="Cantidad: " + str(row[2]))
                        specificDisponibilidad = Label(tab2, text="Disponible: " + row[3])
                        specificTipoPrestamo = Label(tab2, text="Tipo de préstamo: " + row[4])
                        specificDiasPrestamo = Label(tab2, text="Días de préstamo: " + str(row[5]) + "\n")
                        specificNombre.pack(anchor="w")
                        specificAutor.pack(anchor="w")
                        specificCantidad.pack(anchor="w")
                        specificDisponibilidad.pack(anchor="w")
                        specificTipoPrestamo.pack(anchor="w")
                        specificDiasPrestamo.pack(anchor="w")
            
            except Exception as e:
                raise

    # Método cuando se hace clic en Donar
    def donarLibro(self):
        dato1 = inputDonado1.get()
        dato2 = inputDonado2.get()
        dato3 = inputDonado3.get()
        dato4 = inputDonado4.get()

        if dato1 == '' or dato2 == '' or dato3 == '' or dato4 == '':
            mensaje = "Debes ingresar toda la información solicitada."
            textoDonacion['text'] = mensaje
        else:
            sql = "INSERT INTO donaciones(nombreLibro, autor, añoPublicacion, nombreColaborador) values ('{}', '{}', '{}', '{}')".format(dato1, dato2, dato3, dato4)
            try:
                self.cursor.execute(sql)
                self.connection.commit()
                mensaje = "Gracias por tu donación. Por favor, deja el libro dentro del buzón correspondiente."
                textoDonacion['text'] = mensaje
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
titulo = Label(tabOne, text=" \nEstos son todos los libros que tenemos en la biblioteca \n \n")
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
titulo2 = Label(tab2, text="\nEscribe el nombre del libro \n")
titulo2.pack(anchor="w")
inputNombre= Entry(tab2, width = "60", highlightthickness=1)
inputNombre.config(highlightbackground = "#000000", highlightcolor = "#000000")
inputNombre.pack(anchor="w")

botonResultado = Button(tab2, text="Buscar", command=libro1.buscarPorNombre, width="40")
botonResultado.pack(anchor="w")

# Contenido pestaña 3
titulo3 = Label(tab3, text="Ingresa los datos solicitados")
titulo3.place(x=10, y=10)

labelNombreDonado = Label(tab3, text="Nombre del libro")
labelNombreDonado.place(x=10, y=40)
input1 = StringVar()
inputDonado1 = Entry(tab3, textvariable=input1, width="60", highlightthickness=1)
inputDonado1.config(highlightbackground = "#000000", highlightcolor = "#000000")
inputDonado1.place(x=10, y=70)

labelApellidoDonado = Label(tab3, text="Autor")
labelApellidoDonado.place(x=10, y=100)
input2 = StringVar()
inputDonado2 = Entry(tab3, textvariable=input2, width="60", highlightthickness=1)
inputDonado2.config(highlightbackground = "#000000", highlightcolor = "#000000")
inputDonado2.place(x=10, y=130)

labelPublicacionDonado = Label(tab3, text="Año de publicación")
labelPublicacionDonado.place(x=10, y=160)
input3 = StringVar()
inputDonado3 = Entry(tab3, textvariable=input3, width="60", highlightthickness=1)
inputDonado3.config(highlightbackground = "#000000", highlightcolor = "#000000")
inputDonado3.place(x=10, y=190)

labelColaboradorDonado = Label(tab3, text="Tu nombre")
labelColaboradorDonado.place(x=10, y=220)
input4 = StringVar()
inputDonado4 = Entry(tab3, textvariable=input4, width="60", highlightthickness=1)
inputDonado4.config(highlightbackground = "#000000", highlightcolor = "#000000")
inputDonado4.place(x=10, y=250)

botonDonacion = Button(tab3, text="Donar", command=libro1.donarLibro, width="40")
botonDonacion.place(x=10, y=300)

textoDonacion = Label(tab3, text='')
textoDonacion.place(x=10, y=340)

ventanaBiblioteca.mainloop()