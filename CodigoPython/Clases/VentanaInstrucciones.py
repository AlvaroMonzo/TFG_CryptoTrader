import tkinter
from CodigoPython.Clases import VentanaCarga
from binance.client import Client
from CodigoPython.Clases import VentanaEleccion


class VentanaInstrucciones:

    def __init__(self, client):
        self.client = client
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # self.ventana_carga.iniciar_carga()
        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        label_titulo = tkinter.Label(ventana, text="Instrucciones", font=("Times", 20))
        label_titulo.pack()

        label_instrucciones = tkinter.Label(ventana)
        archivo = open("Instrucciones.txt")
        label_instrucciones.configure(text=str(archivo.read()))
        label_instrucciones.pack()

        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana))
        boton_atras.pack()
        # self.ventana_carga.quitar_carga()
        ventana.mainloop()

    def atras(self, ventana):
        ventana.destroy()
        VentanaEleccion.VentanaEleccion(self.client)
