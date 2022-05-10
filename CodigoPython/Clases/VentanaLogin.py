import tkinter

from binance.client import Client
from CodigoPython.Clases import VentanaEleccion

class VentanaLogin:

    client = ""
    def __init__(self):
        self.iniciar_componentes()

    def iniciar_componentes(self):
        ventana = tkinter.Tk()
        ventana.geometry("400x200+100+100")
        ventana.resizable(width=False, height=False)
        ventana.title("CRYPTO TRADER")

        labelAPIkey = tkinter.Label(ventana, text="API Key:")
        labelAPIkey.grid(padx=10, pady=10, row=0, column=0)

        textFieldAPIkey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldAPIkey.grid(padx=10, pady=10, row=0, column=1)
        textFieldAPIkey.insert(0, "WFvHi2sNONLatAPXFueeH1LyiFGFSCa8TKENqDMKY1vz236M6ABnefDxw5dkTGZm")


        labelSecretKey = tkinter.Label(ventana, text="Secret Key:")
        labelSecretKey.grid(padx=10, pady=10, row=1, column=0)

        textFieldSecretKey = tkinter.Entry(ventana, bg="white", width=40)
        textFieldSecretKey.grid(padx=10, pady=10, row=1, column=1)
        textFieldSecretKey.insert(0, "Z45Y85Qn4eN0nJbb2rd6wStVyJcAXd19UbqRgcEEYsCS7NK3QduyHRC3XGSJURBh")

        buttonLogin = tkinter.Button(ventana, text="Login",command=lambda: self.login(textFieldAPIkey, textFieldSecretKey, ventana))
        buttonLogin.grid(rowspan=2, column=2, row=0)

        #ventana.bind('<Return>', self.loginEnter)
        ventana.mainloop()

    def login(self,textFieldAPIkey, textFieldSecretKey, ventana):

        APIkey = textFieldAPIkey.get()
        SecretKey = textFieldSecretKey.get()
        try:
            self.client = Client(APIkey, SecretKey)
        #Hago una solicitud de prueba
            self.client.get_asset_balance(asset='BTC')

            ventana.destroy()
            VentanaEleccion.VentanaEleccion(self.client)

        except:
            cargando_label=tkinter.Label(ventana,text="Error, vuelve a introducir los datos...", fg="red")
            cargando_label.grid(row=2, column=0, columnspan=2)

            print("An exception occurred")
