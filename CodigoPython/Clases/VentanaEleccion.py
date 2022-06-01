import tkinter

from CodigoPython.Clases import VentanaLogin
from CodigoPython.Clases import VentanaEstadisticas
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaInicio
from CodigoPython.Clases import VentanaCarga


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
        boton_estadistica = tkinter.Button(ventana_e, text="Tu cuenta", width=30, height=15,
                                           command=lambda: self.opcion(1, ventana_e))
        boton_estadistica.grid(padx=10, pady=10, row=0, column=0)

        boton_inicio = tkinter.Button(ventana_e, text="Inicio", width=30, height=15,
                                      command=lambda: self.opcion(2, ventana_e))
        boton_inicio.grid(padx=10, pady=10, row=0, column=1)

        boton_instrucciones = tkinter.Button(ventana_e, text="Instrucciones", width=30, height=15,
                                             command=lambda: self.opcion(3, ventana_e))
        boton_instrucciones.grid(padx=10, pady=10, row=0, column=2)

        boton_atras = tkinter.Button(ventana_e, text="Atrás", width=5, height=2,
                                     command=lambda: self.opcion(4, ventana_e))
        boton_atras.grid(padx=10, pady=10, row=0, column=3)

        ventana_e.mainloop()

    def opcion(self, opcion_escogida, ventana_e):
        self.valor = opcion_escogida

        if opcion_escogida == 1:
            ventana_e.destroy()
            VentanaEstadisticas.VentanaEstadisticas(self.client)
        elif opcion_escogida == 2:
            ventana_e.destroy()
            VentanaInicio.VentanaInicio(self.client)
        elif opcion_escogida == 3:
            ventana_e.destroy()
            VentanaInstrucciones.VentanaInstrucciones(self.client,1)

        elif opcion_escogida == 4:
            ventana_e.destroy()
            VentanaLogin.VentanaLogin()
