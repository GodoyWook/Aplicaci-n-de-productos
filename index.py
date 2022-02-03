from tkinter import ttk
from tkinter import *



import sqlite3



class Producto:
    
    nombre_db = "database.db"

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
        self.tabla = ttk.Treeview(height= 10, columns=4)
        self.tabla.grid(row=4, column=0, columnspan=2)
        self.tabla.heading("#0", text="Nombre", anchor=CENTER)
        self.tabla.heading("#1", text="Precio", anchor=CENTER)
        


        self.obtener_productos()

    #Abre la consulta especifica en la base de datos
    def abrir_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.nombre_db) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(consulta, parametros)
            conexion.commit()
        return result

    #adquirir fila específica de la base de datos
    def obtener_productos(self):
        #Limpiando tabla
        record = self.tabla.get_children()
        for element in record:
            self.tree.delete(element)

        #Consultando datos
        consult = "SELECT * FROM producto ORDER BY vto DESC"
        fila_db= self.abrir_consulta(consult)
        
        #Llenando datos
        for fila in fila_db:
            print(fila)

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Producto(ventana)
    ventana.mainloop()
