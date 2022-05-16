import tkinter as tk
from tkinter import ttk

class VentanaCarga(ttk.Frame):

    def __init__(self,mensaje):
        main_window = tk.Tk()
        super().__init__(main_window)
        main_window.title(mensaje)
        self.label_carga = ttk.Label(self, text=mensaje)
        self.label_carga.place(x=30, y=30, width=200)
        self.progressbar = ttk.Progressbar(self, mode="indeterminate")
        self.progressbar.place(x=30, y=60, width=200)
        # Iniciar el movimiento de la barra indeterminada.
        self.progressbar.start()
        self.place(width=300, height=200)
        main_window.geometry("300x200")

    def iniciar_carga(self):
        self.mainloop()

    def quitar_carga(self):
        self.destroy()

