
from tkinter import ttk
from tkinter import *



import sqlite3
from types import CellType

class Producto:

    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title("Aplicación de productos")
        
        #Creacion de contenedor
        cont = LabelFrame(self.vent, text= "Registra un nuevo producto:")
        cont.grid(row= 0, column=0, columnspan=3,pady=20)

        #Nombre
        Label(cont, text = "Nombre: ").grid(row=1, column=0)
        self.nombre = Entry(cont)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1 )

        #Precio
        Label(cont, text="Precio: ").grid(row=2, column=0)
        self.precio = Entry(cont)
        self.precio.grid(row=2, column=1)

        #Botón Agregar producto
        ttk.Button(cont, text="Guardar producto").grid(row=3, columnspan= 2, sticky= W + E)

        #Tabla
        self.tabla= ttk.Treeview(height= 10, columns=2)
        self.tabla.grid(row=4, column=0, columnspan=2)
        self.tabla.heading("#0", text="Nombre", anchor=CENTER)
        self.tabla.heading("#1", text="Precio", anchor=CENTER)

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Producto(ventana)
    ventana.mainloop()
