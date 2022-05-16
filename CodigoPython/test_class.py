import threading
import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen

def download_file_worker():
    url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
    filename = "python-3.7.2.exe"
    # Abrir la dirección de URL.
    with urlopen(url) as r:
        with open(filename, "wb") as f:
            # Leer el archivo remoto y escribir el fichero local.
            f.write(r.read())
def schedule_check(t,root):
    """
    Programar la ejecución de la función `check_if_done()` dentro de un segundo.
    """
    root.after(1000, check_if_done, t,root)
def check_if_done(t,root):
    # Si el hilo ha finalizado, restaruar el botón y mostrar un mensaje.
    if not t.is_alive():
        info_label["text"] = "¡El archivo se ha descargado!"
        # Restablecer el botón.
        download_button["state"] = "normal"
        root.destroy()

    else:
        # Si no, volver a chequear en unos momentos.
        schedule_check(t,root)
def download_file(root):
    info_label["text"] = "Descargando archivo..."
    # Deshabilitar el botón mientras se descarga el archivo.
    download_button["state"] = "disabled"
    # Iniciar la descarga en un nuevo hilo.
    t = threading.Thread(target=download_file_worker)
    t.start()
    # Comenzar a chequear periódicamente si el hilo ha finalizado.
    schedule_check(t,root)
root = tk.Tk()
root.title("Descargar archivo con Tcl/Tk")
info_label = ttk.Label(text="Presione el botón para descargar el archivo.")
info_label.pack()
download_button = ttk.Button(text="Descargar archivo", command=lambda: download_file(root))
download_button.pack()
root.mainloop()


#------------------------------TIMER-------------------
import threading
import time

class Timer(threading.Thread):
    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()
    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def stop(self):
        self._timer_runs.clear()

class HelloWorldTimer(Timer):
    interval = 3   # Intervalo en segundos.

    # Función a ejecutar.
    def timer(self):
        print("¡Hola, mundo!")

hello_world_timer = HelloWorldTimer()
hello_world_timer.start()   # Iniciar el timer.
time.sleep(10)
hello_world_timer.stop()    # Detenerlo.
