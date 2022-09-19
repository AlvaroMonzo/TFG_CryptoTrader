import tkinter

from CodigoPython.Clases import VentanaEstadisticas
from CodigoPython.Clases import VentanaInicio
from CodigoPython.Clases import VentanaInstrucciones
from CodigoPython.Clases import VentanaLogin, VentanaGraficas, VentanaMonedas


class VentanaEleccion:
    valor = ""

    def __init__(self, client):

        #Instanciamos el cliente
        self.client = client
        self.iniciar_componentes()

    def iniciar_componentes(self):

        ventana_e = tkinter.Tk()
        ventana_e.geometry("720x160+100+50")
        ventana_e.resizable(width=False, height=False)
        ventana_e.title("CRYPTO TRADER")
        boton_cuenta = tkinter.Button(ventana_e, text="Tu cuenta",  width=15, height=7,
                                           command=lambda: self.opcion(1, ventana_e))
        boton_cuenta.grid( row=0, column=0)
        boton_inicio = tkinter.Button(ventana_e, text="Inicio",  width=15, height=7,
                                      command=lambda: self.opcion(2, ventana_e))
        boton_inicio.grid( row=0, column=1)

        #Asignamos a cada botón un entero
        boton_instrucciones = tkinter.Button(ventana_e, text="Instrucciones",  width=15, height=7,
                                             command=lambda: self.opcion(3, ventana_e))
        boton_instrucciones.grid(row=0, column=2)

        boton_graficas = tkinter.Button(ventana_e, text="Gráfica", width=15, height=7,
                                             command=lambda: self.opcion(4, ventana_e))
        boton_graficas.grid( row=0, column=3)

        boton_monedas = tkinter.Button(ventana_e, text="Monedas", width=15, height=7,
                                             command=lambda: self.opcion(5, ventana_e))
        boton_monedas.grid( row=0, column=4)

        boton_atras = tkinter.Button(ventana_e, text="Atrás", width=15, height=7,
                                     command=lambda: self.opcion(6, ventana_e))
        boton_atras.grid( row=0, column=5)

        ventana_e.mainloop()

    def opcion(self, opcion_escogida, ventana_e):

        self.valor = opcion_escogida
        #A cada ventana le pasamos el cliente correspondiente
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
            VentanaGraficas.VentanaGraficas(self.client,1)
        elif opcion_escogida == 5:
            ventana_e.destroy()
            VentanaMonedas.VentanaMonedas(self.client,1)
        elif opcion_escogida == 6:
            ventana_e.destroy()
            VentanaLogin.VentanaLogin()
