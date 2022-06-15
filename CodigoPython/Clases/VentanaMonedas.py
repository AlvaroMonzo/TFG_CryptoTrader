import tkinter
from tkinter import ttk

from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInicio

import pandas as pd
import mplfinance as mpf


class VentanaMonedas:

    def __init__(self, client, ventana_proveniente):
        self.client = client
        self.ventana_proveniente = ventana_proveniente
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        lista_criptomonedas = ["BTCUSDT", "AAVEUSDT", "ADAUSDT", "BNBUSDT"]

        boton_atras = tkinter.Button(ventana, text="Atras",
                                     command=lambda: self.atras(ventana, self.ventana_proveniente))
        boton_atras.grid(sticky='SE')

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(sticky='SE')

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        ventana.mainloop()

    def atras(self, ventana, ventana_proveniente):
        ventana.destroy()
        if ventana_proveniente == 1:
            VentanaEleccion.VentanaEleccion(self.client)
        elif ventana_proveniente == 2:
            VentanaInicio.VentanaInicio(self.client)

    def instrucciones(self, ventana):
        ventana.destroy()
        VentanaInstrucciones.VentanaInstrucciones(self.client, 4)
