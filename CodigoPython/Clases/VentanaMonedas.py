import tkinter
from tkinter import ttk

from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInicio

import pandas as pd
import mplfinance as mpf
import requests


class VentanaMonedas:

    def __init__(self, client, ventana_proveniente):
        self.client = client
        self.ventana_proveniente = ventana_proveniente
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana = tkinter.Tk()
        ventana.geometry("1200x580+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        # This example uses Python 2.7 and the python-request library.

        from requests import Request, Session
        from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
        import json

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        #        parameters = {
        #           'start': '1',
        #          'limit': '5000',
        #         'convert': 'USD'
        #    }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '334a6f24-17e0-4efb-ab4d-7033e75af5fd',
        }

        session = Session()
        session.headers.update(headers)

        json = requests.get(url, headers=headers).json()
        monedas = json['data']
        # print(monedas)
        fila = 0

        for moneda in monedas:
            columna = 0
            if float(moneda['cmc_rank']) <= 20:
                label_moneda = tkinter.Label(ventana, text="Símbolo:" + (moneda['symbol']))
                label_moneda.grid(column=columna, row=fila)
                volumen =  moneda['quote']['USD']['volume_24h']
                columna+=1
                if volumen>0.0:
                    label_volumen = tkinter.Label(ventana,text=" Volumen 24h: " + "{:.2f}".format(volumen),fg="lime green")
                    label_volumen.grid(column=columna, row=fila)
                else:
                    label_volumen = tkinter.Label(ventana,text=" Volumen 24h: " + "{:.2f}".format(volumen),fg="firebrick")
                    label_volumen.grid(column=columna, row=fila)

                precio = moneda['quote']['USD']['price']
                columna+=1

                label_volumen = tkinter.Label(ventana,text=" Precio: " + "{:.2f}".format(precio))
                label_volumen.grid(column=columna, row=fila)

                procentaje1h =  moneda['quote']['USD']['percent_change_1h']
                columna+=1
                if procentaje1h>0.0:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 1h: " + "{:.2f}".format(procentaje1h),fg="lime green")
                    label_volumen.grid(column=columna, row=fila)
                else:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 1h: " + "{:.2f}".format(procentaje1h),fg="firebrick")
                    label_volumen.grid(column=columna, row=fila)

                procentaje24h =  moneda['quote']['USD']['percent_change_24h']
                columna+=1
                if procentaje24h>0.0:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 24h: " + "{:.2f}".format(procentaje24h),fg="lime green")
                    label_volumen.grid(column=columna, row=fila)
                else:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 24h: " + "{:.2f}".format(procentaje24h),fg="firebrick")
                    label_volumen.grid(column=columna, row=fila)

                procentaje7d =  moneda['quote']['USD']['percent_change_7d']
                columna+=1
                if procentaje7d>0.0:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 7d: " + "{:.2f}".format(procentaje7d),fg="lime green")
                    label_volumen.grid(column=columna, row=fila)
                else:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 7d: " + "{:.2f}".format(procentaje7d),fg="firebrick")
                    label_volumen.grid(column=columna, row=fila)

                columna+=1
                procentaje30d =  moneda['quote']['USD']['percent_change_30d']
                if procentaje30d>0.0:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 30d: " + "{:.2f}".format(procentaje30d),fg="lime green")
                    label_volumen.grid(column=columna, row=fila)
                else:
                    label_volumen = tkinter.Label(ventana,text=" % de cambio 30d: " + "{:.2f}".format(procentaje30d),fg="firebrick")
                    label_volumen.grid(column=columna, row=fila)


                fila += 1

        boton_atras = tkinter.Button(ventana, text="Atras",
                                     command=lambda: self.atras(ventana, self.ventana_proveniente))
        boton_atras.grid(column=0, row=fila + 1)

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(column=0, row=fila + 2)
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
