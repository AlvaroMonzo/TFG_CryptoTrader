import tkinter

from binance.client import Client
from CodigoPython.Clases import VentanaEleccion


class VentanaLogin:
    client = ""

    def __init__(self):
        # Iniciamos los componentes en el constructor
        self.iniciar_componentes()

    def iniciar_componentes(self):
        # Creamos la ventana
        ventana = tkinter.Tk()
        ventana.geometry("400x150+100+100")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        # Creamos los label

        labelAPIkey = tkinter.Label(ventana, text="API Key:")
        labelAPIkey.grid(padx=10, pady=10, row=0, column=0)

        textFieldAPIkey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldAPIkey.grid(padx=10, pady=10, row=0, column=1)
        textFieldAPIkey.insert(0, "APIKEY")

        labelSecretKey = tkinter.Label(ventana, text="Secret Key:")
        labelSecretKey.grid(padx=10, pady=10, row=1, column=0)

        textFieldSecretKey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldSecretKey.grid(padx=10, pady=10, row=1, column=1)
        textFieldSecretKey.insert(0, "SECREY KEY")

        buttonLogin = tkinter.Button(ventana, text="Login",
                                     command=lambda: self.login(textFieldAPIkey, textFieldSecretKey, ventana))
        buttonLogin.grid(rowspan=2, column=2, row=0)

        # ventana.bind('<Return>', self.loginEnter)
        ventana.mainloop()

    def login(self, textFieldAPIkey, textFieldSecretKey, ventana):

        APIkey = textFieldAPIkey.get()
        SecretKey = textFieldSecretKey.get()

        try:

            # Creamos el objeto cliente, que es el que utilizaremos en todo momento
            self.client = Client(APIkey, SecretKey)
            status = self.client.get_system_status()
            self.client.get_asset_balance(asset='BTC')
            #Si el estado del cliente es 1, estamos en mantenimiento y controlamos la salida.
            #Sino es que el sistema es correcto
            if int(status['status']) == 1:
                raise ValueError("Sistema en mantenimiento, espere un tiempo...")
            else:
                #Borramos la ventana
                ventana.destroy()

                #Mostramos la ventana de elección y le pasamos el cliente
                VentanaEleccion.VentanaEleccion(self.client)

        except ValueError as e:
            cargando_label = tkinter.Label(ventana, text=e, fg="red")
            cargando_label.grid(row=2, column=0, columnspan=2)
        except Exception as e:
            cargando_label = tkinter.Label(ventana, text="Error, vuelve a introducir los datos...", fg="red")
            cargando_label.grid(row=2, column=0, columnspan=2)

            print(e)
