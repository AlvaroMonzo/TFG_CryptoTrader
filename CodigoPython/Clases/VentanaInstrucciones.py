import tkinter
from CodigoPython.Clases import VentanaCarga
from binance.client import Client
from CodigoPython.Clases import VentanaEleccion, VentanaGraficas
from CodigoPython.Clases import VentanaInicio


class VentanaInstrucciones:

    def __init__(self, client, ventana_proveniente):
        self.client = client
        self.ventana_proveniente = ventana_proveniente
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # self.ventana_carga.iniciar_carga()
        ventana = tkinter.Tk()
        ventana.geometry("1200x400+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        label_titulo = tkinter.Label(ventana, text="Instrucciones", font=("Times", 20))
        label_titulo.pack()

        label_instrucciones = tkinter.Label(ventana)
        archivo = open("Instrucciones.txt")
        label_instrucciones.configure(text=str(archivo.read()))
        label_instrucciones.pack()

        boton_atras = tkinter.Button(ventana, text="Atras",
                                     command=lambda: self.atras(ventana, self.ventana_proveniente))
        boton_atras.pack()
        # self.ventana_carga.quitar_carga()
        ventana.mainloop()

    def atras(self, ventana, ventana_proveniente):
        ventana.destroy()
        if ventana_proveniente == 1:
            VentanaEleccion.VentanaEleccion(self.client)
        elif ventana_proveniente == 2:
            VentanaInicio.VentanaInicio(self.client)
        elif ventana_proveniente == 3:
            VentanaGraficas.VentanaGraficas(self.client,1)
