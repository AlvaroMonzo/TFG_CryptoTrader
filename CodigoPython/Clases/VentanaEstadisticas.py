import tkinter

from dateparser.parser import tokenizer

from CodigoPython.Clases import VentanaCarga

from binance.client import Client

from binance.client import *

from CodigoPython.Clases import VentanaEleccion


class VentanaEstadisticas:
    # def __init__(self, client,ventana_carga):
    #    self.client = client
    #    #self.ventana_carga=ventana_carga
    #    self.iniciar_componentes()

    ventana_carga = ""

    def __init__(self, client):
        self.client = client
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # self.ventana_carga.iniciar_carga()

        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")
        print("Inicia la carga")

        label_estadistica = tkinter.Label(ventana, text="Tu cuenta", font=("Times", 20))
        label_estadistica.grid(column=0, row=0)

        cadena_predefinida = "{}: Libre: {} Bloqueado: {} "

        label_btc = tkinter.Label(ventana)
        valor_btc = self.client.get_asset_balance(asset='BTC')
        valor_btc_asset = valor_btc['asset']
        valor_btc_free = valor_btc['free']
        valor_btc_locked = valor_btc['locked']
        label_btc.config(
            text=cadena_predefinida.format(str(valor_btc_asset), str(valor_btc_free), str(valor_btc_locked)))
        label_btc.grid(columnspan=2, column=0, row=1)

        label_eth = tkinter.Label(ventana)
        valor_eth = self.client.get_asset_balance(asset='ETH')
        valor_eth_asset = valor_eth['asset']
        valor_eth_free = valor_eth['free']
        valor_eth_locked = valor_eth['locked']
        label_eth.config(
            text=cadena_predefinida.format(str(valor_eth_asset), str(valor_eth_free), str(valor_eth_locked)))
        label_eth.grid(columnspan=2, column=0, row=2)

        label_usdt = tkinter.Label(ventana)
        valor_usdt = self.client.get_asset_balance(asset='USDT')
        valor_usdt_asset = valor_usdt['asset']
        valor_usdt_free = valor_usdt['free']
        valor_usdt_locked = valor_usdt['locked']
        label_usdt.config(
            text=cadena_predefinida.format(str(valor_usdt_asset), str(valor_usdt_free), str(valor_usdt_locked)))
        label_usdt.grid(columnspan=2, column=0, row=3)

        label_bnb = tkinter.Label(ventana)
        valor_bnb = self.client.get_asset_balance(asset='BNB')
        valor_bnb_asset = valor_bnb['asset']
        valor_bnb_free = valor_bnb['free']
        valor_bnb_locked = valor_bnb['locked']
        label_bnb.config(
            text=cadena_predefinida.format(str(valor_bnb_asset), str(valor_bnb_free), str(valor_bnb_locked)))
        label_bnb.grid(columnspan=2, column=0, row=4)

        label_xrp = tkinter.Label(ventana)
        valor_xrp = self.client.get_asset_balance(asset='XRP')
        valor_xrp_asset = valor_xrp['asset']
        valor_xrp_free = valor_xrp['free']
        valor_xrp_locked = valor_xrp['locked']
        label_xrp.config(
            text=cadena_predefinida.format(str(valor_xrp_asset), str(valor_xrp_free), str(valor_xrp_locked)))
        label_xrp.grid(columnspan=2, column=0, row=5)

        label_sol = tkinter.Label(ventana)
        valor_sol_asset = self.client.get_asset_balance(asset='SOL')['asset']
        valor_sol_free = self.client.get_asset_balance(asset='SOL')['free']
        valor_sol_locked = self.client.get_asset_balance(asset='SOL')['locked']
        label_sol.config(
            text=cadena_predefinida.format(str(valor_sol_asset), str(valor_sol_free), str(valor_sol_locked)))
        label_sol.grid(columnspan=2, column=0, row=6)

        label_ada = tkinter.Label(ventana)
        valor_ada = self.client.get_asset_balance(asset='ADA')
        valor_ada_asset = valor_ada['asset']
        valor_ada_free = valor_ada['free']
        valor_ada_locked = valor_ada['locked']
        label_ada.config(
            text=cadena_predefinida.format(str(valor_ada_asset), str(valor_ada_free), str(valor_ada_locked)))
        label_ada.grid(columnspan=2, column=0, row=7)

        label_doge = tkinter.Label(ventana)
        valor_doge = self.client.get_asset_balance(asset='DOGE')
        valor_doge_asset = valor_doge['asset']
        valor_doge_free = valor_doge['free']
        valor_doge_locked = valor_doge['locked']
        label_doge.config(
            text=cadena_predefinida.format(str(valor_doge_asset), str(valor_doge_free), str(valor_doge_locked)))
        label_doge.grid(columnspan=2, column=0, row=8)

        label_avax = tkinter.Label(ventana)
        valor_avax = self.client.get_asset_balance(asset='AVAX')
        valor_avax_asset = valor_avax['asset']
        valor_avax_free = valor_avax['free']
        valor_avax_locked = valor_avax['locked']
        label_avax.config(
            text=cadena_predefinida.format(str(valor_avax_asset), str(valor_avax_free), str(valor_avax_locked)))
        label_avax.grid(columnspan=2, column=0, row=9)

        label_total_dolares = tkinter.Label(ventana)

        total_dolares = float(self.client.get_symbol_ticker(symbol="ADAUSDT")['price']) * float(valor_ada_free) \
                        + float(self.client.get_symbol_ticker(symbol="AVAXUSDT")['price']) * float(valor_avax_free) \
                        + float(self.client.get_symbol_ticker(symbol="BNBUSDT")['price']) * float(valor_bnb_free) \
                        + float(self.client.get_symbol_ticker(symbol="BTCUSDT")['price']) * float(valor_btc_free) \
                        + float(self.client.get_symbol_ticker(symbol="DOGEUSDT")['price']) * float(valor_doge_free) \
                        + float(self.client.get_symbol_ticker(symbol="ETHUSDT")['price']) * float(valor_eth_free) \
                        + float(self.client.get_symbol_ticker(symbol="SOLUSDT")['price']) * float(valor_sol_free) \
                        + float(self.client.get_symbol_ticker(symbol="TUSDUSDT")['price']) * float(valor_usdt_free) \
                        + float(self.client.get_symbol_ticker(symbol="XRPUSDT")['price']) * float(valor_xrp_free)

        label_total_dolares.configure(text=str(round(total_dolares, 2)) + " $")
        label_total_dolares.grid(column=10, row=0)

        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana))
        boton_atras.grid(columnspan=2, column=10, row=9, sticky="SE")
        # self.ventana_carga.quitar_carga()
        ventana.mainloop()

    def atras(self, ventana):
        ventana.destroy()
        VentanaEleccion.VentanaEleccion(self.client)

