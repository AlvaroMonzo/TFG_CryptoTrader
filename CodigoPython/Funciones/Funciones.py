import tkinter as tk
from tkinter import ttk
from threading import Thread
from urllib.request import urlretrieve, urlcleanup
class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Barra de progreso en Tk")
        self.progressbar = ttk.Progressbar(self)
        self.progressbar.place(x=30, y=60, width=200)
        self.download_button = ttk.Button(
        self, text="Descargar", command=self.download_button_clicked)
        self.download_button.place(x=30, y=20)
        self.place(width=300, height=200)
        main_window.geometry("300x200")


    def download(self):
        # https://recursospython.com/codigos-de-fuente/inyector-de-dll-con-interfaz-grafica/
        url = "https://www.recursospython.com/inyector-de-dll-exe.rar"
        urlretrieve(url, "inyector-de-dll-exe.rar", self.download_status)
        urlcleanup()

    def download_button_clicked(self):
        # Descargar el archivo en un nuevo hilo.
        Thread(target=self.download).start()
        print("Terminado")

    def download_status(self, count, data_size, total_data):
        if count == 0:
            # Establecer el máximo valor para la barra de progreso.
            self.progressbar.configure(maximum=total_data)

        else:
            # Aumentar el progreso.
            self.progressbar.step(data_size)


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
