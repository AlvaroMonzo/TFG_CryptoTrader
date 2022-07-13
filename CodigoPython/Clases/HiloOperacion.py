import threading
import time
import os, platform, logging
import csv
from binance.enums import *

from CodigoPython.Clases import variablesTransitorias


class MiHilo(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        #Creamos el hilo y le asignamos todos los valores correspondientes
        self.capital = args[0]
        self.stop = args[1]
        self.profit = args[2]
        self.subida = args[3]
        self.bajada = args[4]
        self.criptomoneda = args[5]
        self.client = args[6]

        #Valores que utilizaremos dentro de la función run
        self.precio_anterior = ""
        self.precio_actual = ""
        self.precio_superior = ""
        self.precio_inferior = ""
        self.capital_USDT = 0.0
        self.capital_cripto = 0.0
        self.minimo = 0
        self.terminado = False
        self.vender = False
        self.comprar = True
        threading.current_thread().setName(self.criptomoneda)
        print("Se inicia el hilo: " + threading.current_thread().getName())

        #Valores que utilizaremos para exportar el csv
        from datetime import datetime
        self.dia = datetime.now().day
        self.mes = datetime.now().month
        self.anno = datetime.now().year
        self.hora = datetime.now().hour
        self.minuto = datetime.now().minute
        self.datos_csv = []


    def run(self):
        #Asignamos el valor
        self.capital_USDT = self.capital
        self.precio_anterior = float(self.client.get_symbol_ticker(symbol=self.criptomoneda)['price'])
        # Precio por el cual si es mayor venderemos
        self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
        # Precio por el cual si es menor compraremos
        self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
        # LOT_SIZE Cantidad minima de compra
        lot_size = (self.client.get_symbol_info(str(self.criptomoneda))['filters'][2]['minQty'])

        punto_encontrado = False
        fin = False
        decimales = 0
        for i in lot_size:
            if not fin:
                if i == ".":
                    punto_encontrado = True
                    print(i)
                elif punto_encontrado:
                    decimales += 1
                    if int(i) == 1:
                        fin = True
        self.minimo = decimales + 1

        while not self.terminado:
            try:
                #Metemos en el diccionario el diccionario el precio superior y el inferior
                variablesTransitorias.añadirDicc(self.criptomoneda,[self.precio_superior,self.precio_inferior])

                time.sleep(0.2)

                #Precio actual es el precio de la criptomoneda en dolares
                self.precio_actual = float(self.client.get_symbol_ticker(symbol=self.criptomoneda)['price'])

                # Simulacion
                print("-------------------------------------------------------------")
                print("Precio Anterior: " + str(self.precio_anterior))
                print("Precio Superior: " + str(self.precio_superior))
                print("Precio Inferior: " + str(self.precio_inferior))
                print("Precio Actual: " + str(self.precio_actual))
                print("Capital cripto: " + str(self.capital_cripto))
                print("Capital USDT: " + str(self.capital_USDT))

                if (self.precio_actual > self.precio_superior and self.vender):
                    # Ha subido el precio, por lo tanto vendemos y reseteamos los valores
                    # Meter un log de venta
                    print("Vendemos a: " + str(self.precio_actual))
                    n = str(self.capital_cripto)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_venta = (float(n))
                    order = self.client.order_market_sell(
                        symbol=self.criptomoneda,
                        quantity=cantidad_venta)
                    self.capital_USDT = self.precio_actual * self.capital_cripto
                    self.capital_cripto = 0
                    # Reseteamos los valores
                    self.precio_anterior = self.precio_actual
                    self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
                    self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
                    self.vender = False
                    self.comprar = True
                    self.datos_csv = ['Venta',str(cantidad_venta),str(self.precio_actual)]
                    logging.critical('Venta ' + str(self.profit) + ' con ' + str(
                            self.precio_actual * self.capital_cripto) + " $")

                elif (
                        self.precio_actual < self.precio_inferior and self.comprar):  # Ha bajado el precio, por lo tanto compramos y reseteamos los valores
                    # Meter un log de compra
                    print("Compramos a: " + str(self.precio_actual))
                    cantidad_compra = self.capital_USDT / self.precio_actual
                    n = str(cantidad_compra)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_compra = (float(n))
                    print("Cantidad de compra: " + str(cantidad_compra))
                    order = self.client.order_market_buy(
                        symbol=self.criptomoneda,
                        quantity=cantidad_compra)
                    self.capital_cripto = cantidad_compra
                    self.capital_USDT = 0
                    # Reseteamos los valores
                    self.precio_anterior = self.precio_actual
                    self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
                    self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
                    self.vender = True
                    self.comprar = False
                    self.datos_csv = ['Compra',str(cantidad_compra),str(self.precio_actual)]
                    logging.critical('Compra ' + str(cantidad_compra) + ' con ' + str(
                                self.precio_actual * self.capital_cripto) + " $")

                else:
                    if self.vender and self.comprar:
                        print("Esperamos al primer paso")
                    elif self.vender:
                        # Recalulamos el dinero que tenemos
                        print("Dinero actual:" + str(self.precio_actual * self.capital_cripto))
                        if (self.precio_actual * self.capital_cripto) > self.profit:
                            self.terminado = True
                            n = str(self.capital_cripto)
                            n = n[:n.index('.') + self.minimo]
                            cantidad_venta = (float(n))
                            order = self.client.order_market_sell(
                                symbol=self.criptomoneda,
                                quantity=cantidad_venta)
                            self.datos_csv = ['Take profit',str(cantidad_venta),str(self.precio_actual)]

                            logging.critical('Hemos llegado al profit de ' + str(self.profit) + ' con ' + str(
                                self.precio_actual * self.capital_cripto) + " $")
                        elif (self.precio_actual * self.capital_cripto) < self.stop:
                            self.terminado = True
                            n = str(self.capital_cripto)
                            n = n[:n.index('.') + self.minimo]
                            cantidad_venta = (float(n))
                            order = self.client.order_market_sell(
                                symbol=self.criptomoneda,
                                quantity=cantidad_venta)
                            self.datos_csv = ['Stop',str(cantidad_venta),str(self.precio_actual)]
                            logging.critical('Stop ' + str(cantidad_compra) + ' con ' + str(
                                self.precio_actual * self.capital_cripto) + " $")


                        print("Nos toca vender")
                    elif self.comprar:
                        # Recalulamos el dinero que tenemos
                        print("Dinero actual:" + str(self.capital_USDT))
                        if self.capital_USDT > self.profit:
                            self.terminado = True
                            logging.critical('Hemos llegado al profit de ' + str(self.profit) + ' con ' + str(
                                self.capital_USDT) + " $")
                            n = str(self.capital_cripto)
                            n = n[:n.index('.') + self.minimo]
                            cantidad_venta = (float(n))
                            order = self.client.order_market_sell(
                                symbol=self.criptomoneda,
                                quantity=cantidad_venta)
                            self.datos_csv = ['Take profit',str(cantidad_venta),str(self.precio_actual)]
                            logging.critical('Hemos llegado al profit de ' + str(self.profit) + ' con ' + str(
                                self.precio_actual * self.capital_cripto) + " $")

                        elif self.capital_USDT < self.stop:
                            self.terminado = True
                            logging.critical(
                                'Hemos llegado al stop de ' + str(self.stop) + ' con ' + str(self.capital_USDT) + " $")
                            n = str(self.capital_cripto)
                            n = n[:n.index('.') + self.minimo]
                            cantidad_venta = (float(n))
                            order = self.client.order_market_sell(
                                symbol=self.criptomoneda,
                                quantity=cantidad_venta)
                            self.datos_csv = ['Stop',str(cantidad_venta),str(self.precio_actual)]
                            logging.critical('Stop ' + str(cantidad_compra) + ' con ' + str(self.precio_actual) + " $")

                        print("Nos toca comprar")

                time.sleep(0.2)
            except Exception as e:
                print(e)

    def parar_hilo(self):
        self.terminado = True
        variablesTransitorias.diccionario.pop(self.criptomoneda)
        logging.critical("HILO PARADO MANUALMENTE")
        # Creamos el csv con la hora de inicio y la criptomoneda

        path_csv = ('C:'+ '\\'+ 'GK'+ '\\'+ 'TFG_CryptoTrader'+ '\\'+ 'Historial'+ '\\'+ str(str(self.criptomoneda) + '_' + str(self.anno) + '_' + str(self.mes) + '_' + str(self.dia) + '_' + str(self.hora) + '_' + str(self.minuto)) + '.csv')


        myFile = open(path_csv, 'w')
        with myFile:
            fieldnames=["Estado", "Cantidad", "Precio"]
            writer=csv.DictWriter(myFile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.datos_csv)

    def get_capital(self):
        return self.capital

    def getName(self):
        return threading.current_thread().getName()
