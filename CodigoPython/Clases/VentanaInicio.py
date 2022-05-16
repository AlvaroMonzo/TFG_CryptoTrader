import tkinter
from tkinter import ttk
from CodigoPython.Clases import VentanaCarga
from binance.client import Client
from CodigoPython.Clases import VentanaEleccion


class VentanaInicio:

    def __init__(self, client):
        self.client = client
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # self.ventana_carga.iniciar_carga()
        lista_criptomonedas = ["BTC"]
        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")


        # self.ventana_carga.quitar_carga()
        label_capital = tkinter.Label(ventana, text="Introduce el capital: ")
        label_capital.grid(column=0,row=0)
        text_field_capital= tkinter.Entry(ventana)
        text_field_capital.grid(column=1,row=0)

        label_stop = tkinter.Label(ventana, text="Introduce el Stop Lose")
        label_stop.grid(column=0,row=1)
        text_field_stop= tkinter.Entry(ventana)
        text_field_stop.grid(column=1,row=1)

        label_profit = tkinter.Label(ventana, text="Introduce el Take Profit")
        label_profit.grid(column=0,row=2)
        text_field_profit= tkinter.Entry(ventana)
        text_field_profit.grid(column=1,row=2)

        label_criptomoneda= tkinter.Label(ventana,text="Seleccione la criptomoneda: ")
        label_criptomoneda.grid(column=2, row =0)
        combobox_criptomoneda=ttk.Combobox(values= lista_criptomonedas,state="readonly")
        combobox_criptomoneda.grid(column=2,row =1)


        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana))
        boton_atras.grid(sticky='SE')

        ventana.mainloop()

    def atras(self, ventana):
        ventana.destroy()
        VentanaEleccion.VentanaEleccion(self.client)
