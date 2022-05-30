import tkinter

from binance.client import Client
from CodigoPython.Clases import VentanaEleccion
from binance.enums import *



class VentanaLogin:
    client = ""

    def __init__(self):
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana = tkinter.Tk()
        ventana.geometry("400x200+100+100")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        labelAPIkey = tkinter.Label(ventana, text="API Key:")
        labelAPIkey.grid(padx=10, pady=10, row=0, column=0)

        textFieldAPIkey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldAPIkey.grid(padx=10, pady=10, row=0, column=1)
        textFieldAPIkey.insert(0, "WFvHi2sNONLatAPXFueeH1LyiFGFSCa8TKENqDMKY1vz236M6ABnefDxw5dkTGZm")

        labelSecretKey = tkinter.Label(ventana, text="Secret Key:")
        labelSecretKey.grid(padx=10, pady=10, row=1, column=0)

        textFieldSecretKey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldSecretKey.grid(padx=10, pady=10, row=1, column=1)
        textFieldSecretKey.insert(0, "Z45Y85Qn4eN0nJbb2rd6wStVyJcAXd19UbqRgcEEYsCS7NK3QduyHRC3XGSJURBh")

        buttonLogin = tkinter.Button(ventana, text="Login",
                                     command=lambda: self.login(textFieldAPIkey, textFieldSecretKey, ventana))
        buttonLogin.grid(rowspan=2, column=2, row=0)

        # ventana.bind('<Return>', self.loginEnter)
        ventana.mainloop()

    def login(self, textFieldAPIkey, textFieldSecretKey, ventana):

        APIkey = textFieldAPIkey.get()
        SecretKey = textFieldSecretKey.get()
        try:
            self.client = Client(APIkey, SecretKey)
            # Hago una solicitud de prueba
            self.client.get_asset_balance(asset='BTC')
            # klines = self.client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
            # print(klines)
            # print(type(klines))
            print(type(self.client.get_symbol_info('BTCUSDT')['filters'][3]['minNotional']))
            print(self.client.get_symbol_info('BTCUSDT')['filters'][3]['minNotional'])
            orders = self.client.get_open_orders(symbol='BTCUSDT')
            print(orders)
            print(self.client.get_asset_balance(asset='USDT'))
            #order = self.client.order_market_buy(
            #     symbol='ACHUSDT',
            #     quantity=559)

            #order = self.client.order_market_buy(
            #    symbol='BTCUSDT',
            #    quantity=0.00033)

            orders = self.client.get_open_orders(symbol='BTCUSDT')
            print(orders)
            ventana.destroy()
            # print("Tipo de cliente es: " + str(type(self.client)))
            # print(self.client.get_account())
            # print(self.client.get_all_tickers())
            # print(type(self.client.get_all_tickers()))
            ##print(self.client.get_symbol_ticker(symbol="BTCUSDT"))
            # print(type(self.client.get_symbol_ticker(symbol="BTCUSDT")))
            # diccionario = self.client.get_symbol_ticker(symbol="BTCUSDT")
            # print(type(diccionario['price']))
            # miprecio=(float(diccionario['price']))
            # print(miprecio)
            # print(self.client.get_symbol_ticker(symbol="BTCUSDT"))
            # print(self.client.get_symbol_ticker(symbol="BTCUSDT"))
            # print(self.client.get_symbol_ticker(symbol="BTCUSDT"))
            # print(self.client.get_symbol_ticker(symbol="BTCUSDT"))
            # print(self.client.get_symbol_ticker(symbol="BTCUSDT"))


            VentanaEleccion.VentanaEleccion(self.client)

        except Exception as e:
            cargando_label = tkinter.Label(ventana, text="Error, vuelve a introducir los datos...", fg="red")
            cargando_label.grid(row=2, column=0, columnspan=2)

            print(e)
