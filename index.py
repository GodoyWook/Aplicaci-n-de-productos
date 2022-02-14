from cgitb import text
from tkinter import ttk
from tkinter import *



import sqlite3



class Producto:
    
    nombre_db = "data_productos.db"

    def __init__(self, ventana):
        self.vent = ventana
        self.vent.title("Aplicación de productos")
        
        #Creacion de contenedor
        cont = LabelFrame(self.vent, text= "Registra un nuevo producto:")
        cont.grid(row= 0, column=0, columnspan=3,pady=20)

        #Nombre
        Label(cont, text = "Código: ").grid(row=1, column=0)
        self.cod = Entry(cont)
        self.cod.focus()
        self.cod.grid(row=1, column=1 )

        Label(cont, text = "Nombre: ").grid(row=2, column=0)
        self.nombre = Entry(cont)
        self.nombre.grid(row=2, column=1)

        #Costo
        Label(cont, text="Costo: ").grid(row=3, column=0)
        self.costo = Entry(cont)
        self.costo.grid(row=3, column=1)

        #Venta
        Label(cont, text="Venta: ").grid(row=4, column=0)
        self.venta = Entry(cont)
        self.venta.grid(row=4, column=1)

        #Vencimiento
        Label(cont, text="Vto: ").grid(row=5, column=0)
        self.venta = Entry(cont)
        self.venta.grid(row=5, column=1)

        #Botón Agregar producto
        ttk.Button(cont, text="Guardar producto").grid(row=5, columnspan= 2, sticky= W + E)

        #Creacion de la tabla
        self.tabla = ttk.Treeview(columns=( "costo", "venta","vto" ))
        self.tabla.grid(row=6, column=0, columnspan=2)
        self.tabla.column("#0", width=120)
        self.tabla.column("costo", width=80, anchor=CENTER)
        self.tabla.column("venta", width=80, anchor=CENTER)
        self.tabla.column("vto", width=80, anchor=CENTER)

        self.tabla.heading("#0", text= "Nombre", anchor=CENTER)
        self.tabla.heading("costo", text= "Costo", anchor=CENTER)
        self.tabla.heading("venta", text= "Venta", anchor=CENTER)
        self.tabla.heading("vto", text= "Vto", anchor=CENTER)
    
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
        consult = "SELECT * FROM producto ORDER BY vto ASC"
        fila_db = self.abrir_consulta(consult)
        
        #Llenando datos
        for fila in fila_db:
            self.tabla.insert("", 0, text=fila[0], values=("","",fila[3]) )
    


if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Producto(ventana)
    ventana.mainloop()
