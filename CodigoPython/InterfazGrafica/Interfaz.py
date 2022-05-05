import tkinter


<<<<<<< Updated upstream
def ventanaLogin():
        ventana=tkinter.Tk()
        ventana.geometry("1000x1000")
        #etiqueta= tkinter.Label(ventana, text = "hola Mundo", bg = "red")
        #side (BOTTOM, TOP), FILL= tkinter.X , fill = tkinter.Y , expand = True
        #etiqueta.pack()

        #command = lambda: saludo("Álvaro")
        #boton1=tkinter.Button(ventana, text = "Instrucciones", padx = 40 , pady = 60 , command = lambda: saludo("Álvaro"))
        #boton1.pack()
        #boton1 = tkinter.Button(ventana, text="boton 1" , width = 10, height = 5)
        #boton2 = tkinter.Button(ventana, text="boton 2", width = 10, height = 5)
        #boton3 = tkinter.Button(ventana, text="boton 3", width = 10, height = 5)
        #boton1.grid(row = 0 , column = 2)
        #boton2.grid(row=1, column=0)
        #boton3.grid(row=2, column=1)
=======
class VentanaEjemplo:

    def __init__(self,root):
        self.master = root
        root.title("Una simple interfaz gráfica")
        root.configure(background='black')

        self.botonInicio = Button(root, text="INICIAR", command=self.saludar(root))
        self.botonInicio.place(x=250,y=75, width=500, height=250)
>>>>>>> Stashed changes


<<<<<<< Updated upstream
        #ventana.mainloop()
=======
        self.botonSalir = Button(self.master, text="Salir", command=root.quit)
        self.botonSalir .place(x=50,y=350, width=100, height=50)
>>>>>>> Stashed changes

"""
        cajaTexto = tkinter.Entry(ventana)
        cajaTexto.pack()

<<<<<<< Updated upstream
        boton1 = tkinter.Button(ventana, text= "click" , command = lambda :textoDeLaCaja(cajaTexto,etiqueta))
        boton1.pack()

        etiqueta = tkinter.Label(ventana)
        etiqueta.pack()
=======
    def saludar(self,root):
        print("¡Hey!")
        miVentana2=Ventana2(root)
>>>>>>> Stashed changes

        
        print("Esta es la ventana principal")
"""

<<<<<<< Updated upstream

=======

class Ventana2:
    def __init__(self,root):
        self.master = root
        root.title("Una simple interfaz gráfica")
        root.configure(background='red')

        self.botonInicio = Button(root, text="Continuar", command=self.saludar)
        self.botonInicio.place(x=250,y=75, width=500, height=250)
>>>>>>> Stashed changes

def saludo (nombre):
        print("hola bb" + nombre)

<<<<<<< Updated upstream
def textoDeLaCaja(cajaTexto,etiqueta):
        textoCaja= cajaTexto.get()
        etiqueta["text"] = textoCaja
        print(textoCaja)
=======
        self.botonSalir = Button(root, text="Salir", command=root.quit)
        self.botonSalir .place(x=50,y=350, width=100, height=50)

        root.title("CRYPTO-TRADER")
        root.wm_geometry("1000x450")
        root.minsize(1000, 450)

    def saludar(self,root):
        print("¡Ventana2!")
        miVentana2=Ventana2(root)

root = Tk()
miVentana = VentanaEjemplo(root)

root.mainloop()
>>>>>>> Stashed changes
