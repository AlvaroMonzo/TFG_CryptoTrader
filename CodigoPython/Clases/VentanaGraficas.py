import tkinter
from tkinter import ttk

from CodigoPython.Clases import variablesTransitorias
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInicio

import pandas as pd
import mplfinance as mpf



class VentanaGraficas:

    def __init__(self, client, ventana_proveniente):
        self.client = client
        self.ventana_proveniente = ventana_proveniente
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
        lista_criptomonedas = ["BTCUSDT", "AAVEUSDT", "ADAUSDT", "BNBUSDT"]

        label_intervalo = tkinter.Label(ventana, text="Introduce el intervalo")
        label_intervalo.grid(column=0, row=0)

        label_criptomoneda = tkinter.Label(ventana, text="Introduce el par")
        label_criptomoneda.grid(column=1, row=0)

        combobox_intervalo = ttk.Combobox(values=lista_kline_interval, state="readonly")
        combobox_intervalo.grid(column=0, row=1)

        combobox_criptomoneda = ttk.Combobox(values=lista_criptomonedas, state="readonly")
        combobox_criptomoneda.grid(column=1, row=1)

        label_numero_velas = tkinter.Label(ventana, text="Introduce número de velas")
        label_numero_velas.grid(column=2, row=0)
        text_field_numero_velas = tkinter.Entry(ventana)
        text_field_numero_velas.grid(column=2, row=1)
        text_field_numero_velas.insert(0, "100")

        boton_atras = tkinter.Button(ventana, text="Atras",
                                     command=lambda: self.atras(ventana, self.ventana_proveniente))
        boton_atras.grid(sticky='SE')

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(sticky='SE')

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        boton_grafica = tkinter.Button(ventana, text="Ver gráfica",
                                       command=lambda: self.ver_grafica(combobox_intervalo, combobox_criptomoneda,
                                                                        error_label, text_field_numero_velas))
        boton_grafica.grid(sticky='SE')

        ventana.mainloop()

    def ver_grafica(self, combobox_intervalo, combobox_criptomoneda, error_label, text_field_numero_velas):
        try:

            if text_field_numero_velas.get() == "":

                numero_velas = 100

            else:
                numero_velas = int(text_field_numero_velas.get())

            candles = self.client.get_klines(symbol=str(combobox_criptomoneda.get()),
                                             interval=str(combobox_intervalo.get()))
            hist_df = pd.DataFrame(candles)
            hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time',
                               'Quote Asset Volume',
                               'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

            hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time'] / 1000, unit='s')
            hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time'] / 1000, unit='s')

            numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume',
                               'TB Quote Volume']

            hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)
            # tail(100)
            hist_df.set_index('Close Time').tail(numero_velas)
            # two_points = [('2022-06-04', 30000),('2022-06-10', 25000)]

            # tail(120)
            if variablesTransitorias.diccionario:
                for key in variablesTransitorias.diccionario:
                    if key == combobox_criptomoneda.get():
                        valorMaximo = variablesTransitorias.diccionario[key][0]
                        valorMin = variablesTransitorias.diccionario[key][1]
                        mpf.plot(hist_df.set_index('Close Time').tail(numero_velas),
                                 hlines=dict(hlines=[valorMaximo, valorMin], colors=['g', 'r'], linestyle='-.'),
                                 type='candle', style='charles',
                                 volume=True,
                                 title=str(combobox_criptomoneda.get()) + " intervalo de " + (combobox_intervalo.get()),
                                 mav=(10, 20, 30))
                    else:
                        mpf.plot(hist_df.set_index('Close Time').tail(numero_velas),
                                 type='candle', style='charles',
                                 volume=True,
                                 title=str(combobox_criptomoneda.get()) + " intervalo de " + (combobox_intervalo.get()),
                                 mav=(10, 20, 30))

            else:

                mpf.plot(hist_df.set_index('Close Time').tail(numero_velas),
                         type='candle', style='charles',
                         volume=True,
                         title=str(combobox_criptomoneda.get()) + " intervalo de " + (combobox_intervalo.get()),
                         mav=(10, 20, 30))

        except ValueError:
            error_label.grid(sticky='SE')
            error_label.configure(text="El número de velas debe de ser un entero")

        except Exception as e:
            print(e)
            error_label.grid(sticky='SE')
            error_label.configure(text="Introduce correctamente los valores")

    def atras(self, ventana, ventana_proveniente):
        ventana.destroy()
        if ventana_proveniente == 1:
            VentanaEleccion.VentanaEleccion(self.client)
        elif ventana_proveniente == 2:
            VentanaInicio.VentanaInicio(self.client)

    def instrucciones(self, ventana):
        ventana.destroy()
        VentanaInstrucciones.VentanaInstrucciones(self.client, 3)
