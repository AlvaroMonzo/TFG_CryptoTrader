import tkinter

from CodigoPython.Clases import VentanaLogin


class VentanaEleccion:
    valor = ""

    def __init__(self, client):
        self.client = client
        self.iniciar_componentes()

    def iniciar_componentes(self):

        ventana_e = tkinter.Tk()
        ventana_e.geometry("800x280+100+50")
        ventana_e.resizable(width=False, height=False)
        ventana_e.title("CRYPTO TRADER")
        boton_estadistica = tkinter.Button(ventana_e, text="Estadísticas", width=30, height=15,
                                           command=lambda: self.opcion(1, ventana_e))
        boton_estadistica.grid(padx=10, pady=10, row=0, column=0)

        boton_inicio = tkinter.Button(ventana_e, text="Inicio", width=30, height=15,
                                     command=lambda: self.opcion(2, ventana_e))
        boton_inicio.grid(padx=10, pady=10, row=0, column=1)

        boton_instrucciones = tkinter.Button(ventana_e, text="Instrucciones", width=30, height=15,
                                            command=lambda: self.opcion(3, ventana_e))
        boton_instrucciones.grid(padx=10, pady=10, row=0, column=2)

        boton_atras = tkinter.Button(ventana_e, text="Atrás", width=5, height=2, command=lambda: self.opcion(4, ventana_e))
        boton_atras.grid(padx=10, pady=10, row=0, column=3)

        ventana_e.mainloop()

    def opcion(self, opcion_escogida, ventana_e):
        print(self.client.get_asset_balance(asset='BTC'))
        self.valor = opcion_escogida
        ventana_e.destroy()
        if opcion_escogida == 1:
            print("hola")
        elif opcion_escogida == 4:
            VentanaLogin.VentanaLogin()

