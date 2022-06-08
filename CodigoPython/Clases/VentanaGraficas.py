import tkinter
from tkinter import ttk

from CodigoPython.Clases import VentanaLogin
from CodigoPython.Clases import VentanaEstadisticas
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInicio

from matplotlib.pyplot import title
import requests
import json
import pandas as pd
import mplfinance as mpf
from binance.client import Client



class VentanaGraficas:

    def __init__(self, client,ventana_proveniente):
        self.client = client
        self.ventana_proveniente=ventana_proveniente
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        lista_kline_interval = ['1m'
            , '3m'
            , '5m'
            , '15m'
            , '30m'
            , '1h'
            , '2h'
            , '4h'
            , '6h'
            , '8h'
            , '12h'
            , '1d'
            , '3d'
            , '1w'
            , '1M']
        lista_criptomonedas = ["BTCUSDT", "AAVEUSDT","ADAUSDT","BNBUSDT"]

        label_intervalo = tkinter.Label(ventana, text="Introduce el intervalo")
        label_intervalo.grid(column=0, row=0)

        label_criptomoneda = tkinter.Label(ventana, text="Introduce el par")
        label_criptomoneda.grid(column=1, row=0)

        combobox_intervalo = ttk.Combobox(values=lista_kline_interval, state="readonly")
        combobox_intervalo.grid(column=0, row=1)

        combobox_criptomoneda = ttk.Combobox(values=lista_criptomonedas, state="readonly")
        combobox_criptomoneda.grid(column=1, row=1)

        boton_grafica = tkinter.Button(ventana, text="Ver gráfica", command=lambda: self.ver_grafica(combobox_intervalo,combobox_criptomoneda))
        boton_grafica.grid(sticky='SE')

        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana,self.ventana_proveniente))
        boton_atras.grid(sticky='SE')

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(sticky='SE')

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        ventana.mainloop()

    def ver_grafica(self,combobox_intervalo,combobox_criptomoneda):

        candles = self.client.get_klines(symbol=str(combobox_criptomoneda.get()), interval=str(combobox_intervalo.get()))

        hist_df = pd.DataFrame(candles)
        hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume',
                'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

        hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit='s')
        hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit='s')

        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']

        hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)

        hist_df.set_index('Close Time').tail(100)

        mpf.plot(hist_df.set_index('Close Time').tail(120),
                type='candle', style='charles',
                volume=True,
                title=str(combobox_criptomoneda.get()) + " intervalo de "+(combobox_intervalo.get()),
                mav=(10,20,30))


    def atras(self, ventana,ventana_proveniente):
        ventana.destroy()
        if ventana_proveniente == 1:
            VentanaEleccion.VentanaEleccion(self.client)
        elif ventana_proveniente == 2:
            VentanaInicio.VentanaInicio(self.client)

    def instrucciones(self, ventana):
        ventana.destroy()
        VentanaInstrucciones.VentanaInstrucciones(self.client, 3)
