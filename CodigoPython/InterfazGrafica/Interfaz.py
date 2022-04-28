from tkinter import Tk, Label, Button


class VentanaEjemplo:
    def __init__(self,root):
        self.master = root
        root.title("Una simple interfaz gráfica")
        root.configure(background='black')

        self.botonInicio = Button(root, text="INICIAR", command=self.saludar)
        self.botonInicio.place(x=250,y=75, width=500, height=250)

        self.botonInstrucciones = Button(root, text="Instrucciones")
        self.botonInstrucciones.place(x=850,y=350, width=100, height=50)

        self.botonSalir = Button(root, text="Salir", command=root.quit)
        self.botonSalir .place(x=50,y=350, width=100, height=50)

        root.title("CRYPTO-TRADER")
        root.wm_geometry("1000x450")
        root.minsize(1000, 450)

    def saludar(self):
        print("¡Hey!")

        miVentana2=Ventana2(root)


class Ventana2:
    def __init__(self,root):
        self.master = root
        root.title("Una simple interfaz gráfica")
        root.configure(background='red')

        self.botonInicio = Button(root, text="COntinuar", command=self.saludar)
        self.botonInicio.place(x=250,y=75, width=500, height=250)

        self.botonInstrucciones = Button(root, text="Instrucciones")
        self.botonInstrucciones.place(x=850,y=350, width=100, height=50)

        self.botonSalir = Button(root, text="Salir", command=root.quit)
        self.botonSalir .place(x=50,y=350, width=100, height=50)

        root.title("CRYPTO-TRADER")
        root.wm_geometry("1000x450")
        root.minsize(1000, 450)

    def saludar(self):
        print("¡Hey!")
        miVentana2=Ventana2(root)

root = Tk()
miVentana = VentanaEjemplo(root)

root.mainloop()
