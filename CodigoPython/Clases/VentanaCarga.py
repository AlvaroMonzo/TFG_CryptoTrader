import threading
import tkinter
from tkinter import ttk

class VentanaCarga(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)


    def run(self):
        '''
        self.ventana_e.mainloop()
        '''
        print("Carga run")
        self.ventana_e=tkinter.Tk()
        self.ventana_e.geometry("300x280+100+50")
        self.ventana_e.resizable(width=False, height=False)
        self.ventana_e.title("Cargando...")
        label_carga = tkinter.Label(self.ventana_e, text="Cargando...")
        label_carga.place(x=30, y=30, width=200)
        progressbar = ttk.Progressbar(self.ventana_e, mode="indeterminate")
        progressbar.place(x=30, y=60, width=200)
        progressbar.start()
        self.ventana_e.mainloop()
    def quitar_carga(self):

        self.ventana_e.destroy()
        print("Descarga run")
        #self.ventana_e.destroy()

