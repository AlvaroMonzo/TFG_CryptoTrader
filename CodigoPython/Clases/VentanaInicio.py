import tkinter
from tkinter import ttk
from CodigoPython.Clases import VentanaCarga
from binance.client import Client
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import HiloOperacion


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
        label_capital.grid(column=0, row=0)
        text_field_capital = tkinter.Entry(ventana)
        text_field_capital.grid(column=1, row=0)

        label_stop = tkinter.Label(ventana, text="Introduce el Stop Lose")
        label_stop.grid(column=0, row=1)
        text_field_stop = tkinter.Entry(ventana)
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
        combobox_criptomoneda = ttk.Combobox(values=lista_criptomonedas, state="readonly")
        combobox_criptomoneda.grid(column=2, row=1)

        boton_atras = tkinter.Button(ventana, text="Atras", command=lambda: self.atras(ventana))
        boton_atras.grid(sticky='SE')

        boton_instrucciones = tkinter.Button(ventana, text="Instrucciones", command=lambda: self.instrucciones(ventana))
        boton_instrucciones.grid(sticky='SE')

        error_label = tkinter.Label(ventana, text="Datos introducidos incorrectos.", fg="red")
        error_label.grid_forget()

        boton_inicio = tkinter.Button(ventana, text="Inicio", command=lambda: self.inicio(ventana,text_field_capital,text_field_stop,text_field_profit,text_field_proc_subida,text_field_proc_bajada,combobox_criptomoneda,error_label))
        boton_inicio.grid(sticky='SE')

        ventana.mainloop()

    def atras(self, ventana):
        ventana.destroy()
        VentanaEleccion.VentanaEleccion(self.client)

    def inicio(self,ventana, capital, stop, profit, subida, bajada, criptomoneda,error_label):

        #Control de entradas
        try:
            capital_value= float(capital.get())
            stop_value= float(stop.get())
            profit_value= float(profit.get())
            subida_value= float(subida.get())
            bajada_value= float(bajada.get())
            criptomoneda_value= str(criptomoneda.get())
            print(capital_value,stop_value,profit_value,subida_value,bajada_value,criptomoneda_value)


            raise Exception('spam', 'eggs')

            print("Los datos son correctos")
            #Creamos un hilo que se encargara de realizar las operaciones.
            hilo=HiloOperacion.MiHilo(args=(capital_value,stop_value,profit_value,subida_value,bajada_value,criptomoneda_value), daemon=False)
            hilo.start()

        except Exception as e:
            print("hola")

        except:
            error_label.grid(sticky='SE')
            print("Fallo en la conversion")


    def instrucciones(self,ventana):
        ventana.destroy()
        VentanaInstrucciones.VentanaInstrucciones(self.client,2)
