import tkinter
from tkinter import ttk

class VentanaCarga():

    def __init__(self):
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana_e = tkinter.Tk()
        ventana_e.geometry("800x280+100+50")
        ventana_e.resizable(width=False, height=False)
        ventana_e.title("Cargando...")
        label_carga = tkinter.Label(ventana_e, text="Cargando...")
        label_carga.place(x=30, y=30, width=200)
        progressbar = ttk.Progressbar(ventana_e, mode="indeterminate")
        progressbar.place(x=30, y=60, width=200)
        # Iniciar el movimiento de la barra indeterminada.
        progressbar.start()
        ventana_e.mainloop()
        print("hola")
    def iniciar_carga(self,ventana_e):
        print("salta aqui?")
        ventana_e.mainloop()

    def quitar_carga(self,ventana_e):
        ventana_e.destroy()

