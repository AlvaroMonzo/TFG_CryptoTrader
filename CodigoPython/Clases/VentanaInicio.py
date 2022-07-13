import tkinter
from tkinter import ttk

from yarl._url import cached_property
from CodigoPython.Clases import VentanaCarga, VentanaGraficas
from binance.client import Client

from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import HiloOperacion

hilos = []  # Listado de hilos activos
fila_label = 0  # Fila de cada hilo


class VentanaInicio:

    def __init__(self, client):
        # Instanciamos el cliente y obtenemos la cantidad de
        # dolares que tenemos en la cuenta
        global fila_label, hilos
        self.client = client
        self.capital_USDT_disponible = float(self.client.get_asset_balance(asset='USDT')['free'])
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # self.ventana_carga.iniciar_carga()
        global fila_label, hilos
        # Creamos un pequeño listado e iniciamos la ventana
        lista_criptomonedas = ["BTCUSDT", "AAVEUSDT", "ADAUSDT", "BNBUSDT"]
        ventana = tkinter.Tk()
        ventana.geometry("800x280+100+50")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        label_capital = tkinter.Label(ventana, text="Introduce el capital: ")
        label_capital.grid(column=0, row=0)
        text_field_capital = tkinter.Entry(ventana)
        text_field_capital.grid(column=1, row=0)

        label_stop = tkinter.Label(ventana, text="Introduce el Stop Lose")
        label_stop.grid(column=0, row=1)
        text_field_stop = tkinter.Entry(ventana)
        text_field_stop.grid(column=1, row=1)
        text_field_stop.grid(column=1, row=1)

        label_profit = tkinter.Label(ventana, text="Introduce el Take Profit")
        label_profit.grid(column=0, row=2)
        text_field_profit = tkinter.Entry(ventana)
        text_field_profit.grid(column=1, row=2)

        label_porc_subida = tkinter.Label(ventana, text="Introduce el porcentaje de venta")
        label_porc_subida.grid(column=0, row=3)
        text_field_proc_subida = tkinter.Entry(ventana)
        text_field_proc_subida.grid(column=1, row=3)

        label_porc_bajada = tkinter.Label(ventana, text="Introduce el porcentaje de compra")
        label_porc_bajada.grid(column=0, row=4)
        text_field_proc_bajada = tkinter.Entry(ventana)
        text_field_proc_bajada.grid(column=1, row=4)

        label_criptomoneda = tkinter.Label(ventana, text="Seleccione la criptomoneda: ")
        label_criptomoneda.grid(column=2, row=0)

        self.combobox_criptomoneda = ttk.Combobox(values=lista_criptomonedas, state="readonly")
        # Cada vez que cambiamos el combobox, miramos el valor minimo para invertir de la criptomoneda asociada
        self.combobox_criptomoneda.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combobox_criptomoneda.grid(column=2, row=1)

        self.label_min_capital = tkinter.Label(ventana, text="Capital mínimo: ")
        self.label_min_capital.grid(column=2, row=2)

        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana))
        boton_atras.grid(sticky='SE')

        boton_grafica = tkinter.Button(ventana, text="Ver gráfica", command=lambda: self.ver_graficas(ventana))
        boton_grafica.grid(sticky='SE')

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(sticky='SE')

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        #Le pasamos los parámetros introducidos para crear el hilo
        boton_inicio = tkinter.Button(ventana, text="Inicio",
                                      command=lambda: self.inicio(ventana, text_field_capital, text_field_stop,
                                                                  text_field_profit, text_field_proc_subida,
                                                                  text_field_proc_bajada, self.combobox_criptomoneda,
                                                                  error_label, label_USDT))
        boton_inicio.grid(sticky='SE')

        # Datos que pongo yo:
        text_field_capital.insert(0, 12)
        text_field_proc_bajada.insert(0, 1)
        text_field_proc_subida.insert(0, 1)
        text_field_profit.insert(0, 13)
        text_field_stop.insert(0, 11)

        # Recorremos la lista de hilos
        for i in range(len(hilos)):
            fila_label = 0
            # Por cada hilo creamos un label
            label_hilo = tkinter.Label(ventana, text="Hilo ejecutando: " + hilos[i].getName())
            label_hilo.grid(column=3, row=fila_label)
            # Y un boton
            boton_parar = tkinter.Button(ventana, text="Parar",
                                         command=lambda: self.parar_hilo(hilos[i], label_hilo, boton_parar,
                                                                         hilos[i].get_capital(),
                                                                         label_USDT))
            boton_parar.grid(column=4, row=fila_label)
            # Restamos al total de dolares disponibles el capital de cada hilo
            self.capital_USDT_disponible -= hilos[i].get_capital()
            fila_label += 1

        label_USDT = tkinter.Label(ventana, text="USTD actuales: " + str(
            round(self.capital_USDT_disponible, 2)))
        label_USDT.grid(column=0, row=5)

        ventana.mainloop()

    def atras(self, ventana):
        ventana.destroy()
        VentanaEleccion.VentanaEleccion(self.client)

    def inicio(self, ventana, capital, stop, profit, subida, bajada, criptomoneda, error_label, label_USDT):
        global fila_label, hilos
        try:
            capital_value = float(capital.get())
            stop_value = float(stop.get())
            profit_value = float(profit.get())
            subida_value = float(subida.get())
            bajada_value = float(bajada.get())
            criptomoneda_value = str(criptomoneda.get())
            precio_min = float(
                self.client.get_symbol_info(str(self.combobox_criptomoneda.get()))['filters'][3]['minNotional'])


            #Comprobamos que la entrada de campos son correctos. Es decir, el precio minimo
            # debe ser superior la mínimo de la compra de la criptomoneda

            if precio_min > capital_value or precio_min > stop_value or precio_min > profit_value:
                raise Exception("Los datos deben ser mayores al precio mínimo")
            if profit_value < capital_value:
                raise Exception("El profit debe ser mayor que el capital")
            if stop_value > capital_value:
                raise Exception("El capital debe ser mayor al stop")
            if not criptomoneda_value:
                raise Exception("Seleccione la criptomoneda")
            #Solo podemos hacer un hilo por inversión
            for i in range(len(hilos)):
                if hilos[i].getName() == criptomoneda_value:
                    raise Exception("Ya tenemos ese hilo ejecutandose")
            if capital_value > self.capital_USDT_disponible:
                raise Exception("Capital insuficiente")

            # Creamos un hilo que se encargara de realizar las operaciones.
            hilo = HiloOperacion.MiHilo(args=(
                capital_value, stop_value, profit_value, subida_value, bajada_value, criptomoneda_value, self.client),
                daemon=False)
            hilo.start()
            hilos.append(hilo)
            #Mostramos el hilo ejecutando
            label_hilo = tkinter.Label(ventana, text="Hilo ejecutando: " + hilo.getName())
            label_hilo.grid(column=3, row=fila_label)

            self.capital_USDT_disponible -= capital_value
            self.repintar_USDT(label_USDT)

            boton_parar = tkinter.Button(ventana, text="Parar",
                                                 command=lambda: self.parar_hilo(hilo, label_hilo, boton_instrucciones,
                                                                                 capital_value,
                                                                                 label_USDT))
            boton_parar.grid(column=4, row=fila_label)

            fila_label += 1
            error_label.grid_forget()

        except Exception as e:
            error_label.grid(sticky='SE')
            error_label.configure(text=e)
        # Control de entradas

    def selection_changed(self, event):
        global fila_label, hilos
        #Cada vez que cambiamos un valor del combobox, realizamos una consulta al cliente para saber el capital mínimo
        selection = self.combobox_criptomoneda.get()
        precio_min = (self.client.get_symbol_info(str(selection))['filters'][3]['minNotional'])
        self.label_min_capital.configure(text="Capital mínimo: " + str(round(float(precio_min), 2)) + " $")

    def parar_hilo(self, hilo, label_hilo, boton_instrucciones, capital_value, label_USDT):
        global fila_label, hilos
        #Obtenemos el hilo y lo paramos
        hilo.parar_hilo()
        label_hilo.destroy()
        boton_instrucciones.destroy()
        fila_label -= 1
        hilos.remove(hilo)

        #Añadimos el capital que tenia el hilo
        self.capital_USDT_disponible = self.capital_USDT_disponible + capital_value
        self.repintar_USDT(label_USDT)

    def instrucciones(self, ventana):
        ventana.destroy()
        VentanaInstrucciones.VentanaInstrucciones(self.client, 2)

    def ver_graficas(self, ventana):
        ventana.destroy()
        VentanaGraficas.VentanaGraficas(self.client, 2)

    def repintar_USDT(self, label_USDT):
        label_USDT.configure(
            text="USTD disponible: " + str(round(float(self.capital_USDT_disponible), 2)))
