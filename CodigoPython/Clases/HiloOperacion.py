import threading
import time

import pandas as pd

from CodigoPython.Clases import variablesTransitorias


class MiHilo(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        # Creamos el hilo y le asignamos todos los valores correspondientes
        self.capital = args[0]
        self.stop = args[1]
        self.profit = args[2]
        self.subida = args[3]
        self.bajada = args[4]
        self.criptomoneda = args[5]
        self.client = args[6]

        # Valores que utilizaremos dentro de la función run
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
        self.calculo_beneficios = 0.0
        self.calculo_beneficiosUSDT = 0.0
        threading.current_thread().setName(self.criptomoneda)
        print("Se inicia el hilo: " + threading.current_thread().getName())

        # Valores que utilizaremos para exportar el csv
        from datetime import datetime
        self.dia = datetime.now().day
        self.mes = datetime.now().month
        self.anno = datetime.now().year
        self.hora = datetime.now().hour
        self.minuto = datetime.now().minute

        self.df = pd.DataFrame(columns=["Estado", "Cantidad", "Precio"])

    def run(self):
        # Asignamos el valor
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
                # Metemos en el diccionario el diccionario el precio superior y el inferior
                variablesTransitorias.annadirDicc(self.criptomoneda, [self.precio_superior, self.precio_inferior])

                # Cada 200 milisegundos realizamos una comprobación del precio
                time.sleep(0.2)
                self.precio_actual = float(self.client.get_symbol_ticker(symbol=self.criptomoneda)['price'])

                # Simulación
                print("-------------------------------------------------------------")
                print("Precio Anterior: " + str(self.precio_anterior))
                print("Precio Superior: " + str(self.precio_superior))
                print("Precio Inferior: " + str(self.precio_inferior))
                print("Precio Actual: " + str(self.precio_actual))
                print("Capital cripto: " + str(self.capital_cripto))
                print("Capital USDT: " + str(self.capital_USDT))
                #print("Calculo beneficios USDT: " + str(self.calculo_beneficiosUSDT))
                #print("Calculo beneficios final: " + str(self.calculo_beneficios))

                # Baja el precio y compramos
                if self.precio_actual < self.precio_inferior and self.comprar:

                    # Calculamos la cantidad que vamos a comprar
                    self.calculo_beneficiosUSDT = self.capital_USDT
                    cantidad_compra = self.capital_USDT / self.precio_actual
                    n = str(cantidad_compra)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_compra = (float(n))

                    # Realizamos la orden
                    order = self.client.order_market_buy(
                        symbol=self.criptomoneda,
                        quantity=cantidad_compra)

                    print("Compramos a:" + str(self.precio_actual) + " una cantidad de: " + str(cantidad_compra))

                    # Una vez con la orden realizada, recalulamos valores.
                    self.capital_cripto = cantidad_compra
                    self.capital_USDT = 0

                    self.precio_anterior = self.precio_actual
                    self.precio_inferior = self.precio_actual - self.precio_anterior * self.bajada
                    self.precio_superior = self.precio_actual + self.precio_anterior * self.subida

                    # Pasamos al estado venta
                    self.vender = True
                    self.comprar = False

                    # Almacenamos este movimiento en un CSV
                    self.df = self.df.append(
                        {"Estado": "Compra", "Cantidad": str(cantidad_compra), "Precio": str(self.precio_actual)},
                        ignore_index=True)
                    print("Estado compra")
                    print(self.df)

                # Sube el precio y vendemos
                elif self.precio_actual > self.precio_superior and self.vender:

                    # Calculamos la cantidad de venta
                    n = str(self.capital_cripto)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_venta = (float(n))

                    # Hacemos la orden de venta
                    order = self.client.order_market_sell(
                        symbol=self.criptomoneda,
                        quantity=cantidad_venta)

                    print("Vendemos a:" + str(self.precio_actual) + " una cantidad de: " + str(cantidad_venta))

                    # Una vez con la orden realizada, recalulamos valores.
                    self.capital_USDT = self.precio_actual * self.capital_cripto
                    self.calculo_beneficios += self.calculo_beneficiosUSDT - self.capital_USDT
                    self.calculo_beneficiosUSDT = 0
                    self.capital_cripto = 0

                    self.precio_anterior = self.precio_actual
                    self.precio_inferior = self.precio_actual - self.precio_anterior * self.bajada
                    self.precio_superior = self.precio_actual + self.precio_anterior * self.subida

                    # Pasamos al estado de compra
                    self.comprar = True
                    self.vender = False

                    # Almacenamos el movimiento en un CSV
                    self.df = self.df.append(
                        {"Estado": "Venta", "Cantidad": str(cantidad_venta), "Precio": str(self.precio_actual)},
                        ignore_index=True)

                    print("Salta la venta")
                    print(self.df)

                    # Si vendemos y tenemos el profit, hemos conseguido el objetivo
                    # Terminaremos el hilo y lo cerraremos
                    if self.calculo_beneficios + self.capital_USDT >= self.profit:
                        print("Salto el take profit")

                        # Almacenamos el movimiento
                        self.df = self.df.append({"Estado": "Take Profit", "Cantidad": str(cantidad_venta),
                                                  "Precio": str(self.precio_actual)}, ignore_index=True)
                        print("Salta el profit")
                        print(self.df)
                        # Paramos el hilo
                        self.parar_hilo()

                # Si estamos para vender y no para de bajar, deberá saltar el stop loose
                elif self.vender and (self.capital_cripto * self.precio_actual) < self.stop:

                    # Vendemos las criptomonedas que tengamos
                    print("Salto el stop loose")

                    # Calculamos la cantidad de venta
                    n = str(self.capital_cripto)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_venta = (float(n))

                    # Hacemos la orden de venta
                    order = self.client.order_market_sell(
                        symbol=self.criptomoneda,
                        quantity=cantidad_venta)

                    # Almacenamos el movimiento
                    self.df = self.df.append(
                        {"Estado": "Stop loose", "Cantidad": str(self.precio_actual * self.capital_cripto),
                         "Precio": str(self.precio_actual)}, ignore_index=True)
                    print("salta stop")
                    print(self.df)
                    # Paramos el hilo
                    self.parar_hilo()
                '''
                
                if self.precio_actual>self.precio_superior and self.vender:
                    #Vendemos lo que tenemos a precio de mercado.
                    print("Vendemos a: " + str(self.precio_actual))
                    #Calulamos el mínimo
                    n = str(self.capital_cripto)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_venta = (float(n))
                    #Y realizamos la orden de venta
                    order = self.client.order_market_sell(
                        symbol=self.criptomoneda,
                        quantity=cantidad_venta)
                    self.
                '''


            except Exception as e:
                print(e)

        '''
        while not self.terminado:
            try:
                # Metemos en el diccionario el diccionario el precio superior y el inferior
                variablesTransitorias.aadirDicc(self.criptomoneda, [self.precio_superior, self.precio_inferior])

                time.sleep(0.2)

                # Precio actual es el precio de la criptomoneda en dolares
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
                    # Ha subido el precio respecto al de referencia, por lo tanto vendemos y reseteamos los valores
                    # print("Vendemos a: " + str(self.precio_actual))
                    # n = str(self.capital_cripto)
                    #  n = n[:n.index('.') + self.minimo]
                    #cantidad_venta = (float(n))
                    #order = self.client.order_market_sell(
                    #    symbol=self.criptomoneda,
                    #    quantity=cantidad_venta)
                    #self.capital_USDT = self.precio_actual * self.capital_cripto
                    #self.capital_cripto = 0
                    # Reseteamos los valores
                    #self.precio_anterior = self.precio_actual
                    #self.precio_superior = self.precio_anterior + self.precio_anterior * self.subida
                    #self.precio_inferior = self.precio_anterior - self.precio_anterior * self.bajada
                    #self.vender = False
                    #self.comprar = True
                    #self.datos_csv = ['Venta', str(cantidad_venta), str(self.precio_actual)]

                elif (self.precio_actual < self.precio_inferior and self.comprar):
                    # Ha bajado el precio, por lo tanto compramos y reseteamos los valores
                    cantidad_compra = self.capital_USDT / self.precio_actual
                    n = str(cantidad_compra)
                    n = n[:n.index('.') + self.minimo]
                    cantidad_compra = (float(n))
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
                    self.datos_csv = ['Compra', str(cantidad_compra), str(self.precio_actual)]
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
                            self.datos_csv = ['Take profit', str(cantidad_venta), str(self.precio_actual)]

                        elif (self.precio_actual * self.capital_cripto) < self.stop:
                            self.terminado = True
                            n = str(self.capital_cripto)
                            n = n[:n.index('.') + self.minimo]
                            cantidad_venta = (float(n))
                            order = self.client.order_market_sell(
                                symbol=self.criptomoneda,
                                quantity=cantidad_venta)
                            self.datos_csv = ['Stop', str(cantidad_venta), str(self.precio_actual)]
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
                            self.datos_csv = ['Take profit', str(cantidad_venta), str(self.precio_actual)]
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
                            self.datos_csv = ['Stop', str(cantidad_venta), str(self.precio_actual)]
                            logging.critical('Stop ' + str(cantidad_compra) + ' con ' + str(self.precio_actual) + " $")

                        print("Nos toca comprar")

                time.sleep(0.2)
            except Exception as e:
                print(e)
'''

    def parar_hilo(self):
        self.terminado = True
        variablesTransitorias.diccionario.pop(self.criptomoneda)
        # Creamos el csv con la hora de inicio y la criptomoneda
        # path_csv = ('C:' + '\\' + 'GK' + '\\' + 'TFG_CryptoTrader' + '\\' + 'Historial' + '\\' + str(
        #     str(self.criptomoneda) + '_' + str(self.anno) + '_' + str(self.mes) + '_' + str(self.dia) + '_' + str(
        #         self.hora) + '_' + str(self.minuto)) + '.csv')

        self.df.to_csv(
            str(str(self.criptomoneda) + '_' + str(self.anno) + '_' + str(self.mes) + '_' + str(self.dia) + '_' + str(
                self.hora) + '_' + str(self.minuto)) + '.csv', sep=";", index=False)

        print(self.df)

    def get_capital(self):
        print("pasa por get_capital")
        return self.capital

    def getName(self):
        return threading.current_thread().getName()
