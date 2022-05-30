import threading
import time
import os, platform, logging
from binance.enums import *


class MiHilo(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.capital = args[0]
        self.stop = args[1]
        self.profit = args[2]
        self.subida = args[3]
        self.bajada = args[4]
        self.criptomoneda = args[5]
        self.client = args[6]
        self.precio_anterior = ""
        self.precio_actual = ""
        self.precio_superior = ""
        self.precio_inferior = ""
        self.capital_USDT = 0.0
        self.capital_cripto = 0.0

        # Haremos que siempre compre primero, por lo tanto deberiamos tener todo en usdt
        self.vender = False
        self.comprar = True
        threading.current_thread().setName("Hilo 1")
        print("Se inicia el hilo: " + threading.current_thread().getName())

        logging.basicConfig(filename=threading.current_thread().getName() + '.log', level=logging.INFO, filemode='w',
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info("El hilo " + threading.current_thread().getName() + " empezó a ejecutarse")

    def run(self):
        # t=0
        terminado = False
        # Simulación:
        self.capital_USDT=self.capital
        # Par de btc con usdt
        self.precio_anterior = float(self.client.get_symbol_ticker(symbol="BTCUSDT")['price'])
        # Precio por el cual si es mayor venderemos
        self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
        # Precio por el cual si es menor compraremos
        self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada

        while not terminado:
            try:

                time.sleep(0.2)
                self.precio_actual = float(self.client.get_symbol_ticker(symbol="BTCUSDT")['price'])

                # Simulacion
                print("-------------------------------------------------------------")
                print("Precio Anterior: " + str(self.precio_anterior))
                print("Precio Superior: " + str(self.precio_superior))
                print("Precio Inferior: " + str(self.precio_inferior))
                print("Precio Actual: " + str(self.precio_actual))
                print("Capital cripto: " + str(self.capital_cripto))
                print("Capital USDT: " + str(self.capital_USDT))

                if (
                        self.precio_actual > self.precio_superior and self.vender):  # Ha subido el precio, por lo tanto vendemos y reseteamos los valores
                    # Meter un log de venta
                    print("Vendemos a: " + str(self.precio_actual))
                    n = str(self.capital_cripto)
                    n=n[:n.index('.')+6]
                    cantidad_venta=(float(n))
                    order = self.client.order_market_sell(
                        symbol='BTCUSDT',
                        quantity=cantidad_venta)
                    self.capital_USDT = self.precio_actual * self.capital_cripto
                    self.capital_cripto=0
                    # Reseteamos los valores
                    self.precio_anterior = self.precio_actual
                    self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
                    self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
                    self.vender = False
                    self.comprar = True
                    logging.warning('Vendemos a: ' + str(self.precio_actual)+ " Dinero actual: " + str(self.capital_USDT))

                elif (
                        self.precio_actual < self.precio_inferior and self.comprar):  # Ha bajado el precio, por lo tanto compramos y reseteamos los valores
                    # Meter un log de compra
                    print("Compramos a: " + str(self.precio_actual))
                    cantidad_compra= self.capital_USDT / self.precio_actual
                    n = str(cantidad_compra)
                    n=n[:n.index('.')+6]
                    cantidad_compra=(float(n))
                    print("Cantidad de compra: " + str(cantidad_compra))
                    order = self.client.order_market_buy(
                        symbol='BTCUSDT',
                        quantity=cantidad_compra)
                    self.capital_cripto = self.capital_USDT / self.precio_actual
                    self.capital_USDT=0
                    # Reseteamos los valores
                    self.precio_anterior = self.precio_actual
                    self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
                    self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
                    self.vender = True
                    self.comprar = False
                    logging.warning('Compramos a: ' + str(self.precio_actual) + " Dinero actual: " + str(self.precio_actual * self.capital_cripto))
                else:
                    if self.vender and self.comprar:
                        print("Esperamos al primer paso")
                    elif self.vender:
                        # Recalulamos el dinero que tenemos
                        print("Dinero actual:" + str(self.precio_actual * self.capital_cripto))
                        print("Nos toca vender")
                    elif self.comprar:
                        # Recalulamos el dinero que tenemos
                        print("Dinero actual:" + str(self.capital_USDT))
                        print("Nos toca comprar")

                time.sleep(0.2)
            except Exception as e:
                print(e)

