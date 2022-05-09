import tkinter

from binance.client import Client

#Ventana login

def ventanaLogin():
    global client,textFieldAPIkey, textFieldSecretKey, ventana
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

    buttonLogin = tkinter.Button(ventana, text="Login",
                                 command=lambda: login(textFieldAPIkey, textFieldSecretKey, ventana))
    buttonLogin.grid(rowspan=2, column=2, row=0)

    ventana.bind('<Return>', loginEnter)
    ventana.mainloop()
    return client

def login(textFieldAPIkey, textFieldSecretKey, ventana):
    global client
    APIkey = textFieldAPIkey.get()
    SecretKey = textFieldSecretKey.get()
    print("Api key = " + APIkey)
    print("Secret Key = " + SecretKey)
    try:
        client = Client(APIkey, SecretKey)
        #Hago una solicitud de prueba
        client.get_asset_balance(asset='BTC')
        ventana.destroy()
    except:
        cargandoLabel=tkinter.Label(ventana,text="Error, vuelve a introducir los datos...", fg="red")
        cargandoLabel.grid(row=2, column=0, columnspan=2)

        print("An exception occurred")

def loginEnter(event):

    login(textFieldAPIkey, textFieldSecretKey, ventana)

#Eleccion

def ventanaEleccion(client):

    global valor

    ventanaE=tkinter.Tk()
    ventanaE.geometry("800x280+100+50")
    ventanaE.resizable(width=False, height=False)
    ventanaE.title("CRYPTO TRADER")

    botonEstadisticas=tkinter.Button(ventanaE,text="Estadísticas", width = 30, height = 15,command=lambda: opcion(1,ventanaE))
    botonEstadisticas.grid(padx=10, pady=10,row=0,column=0)

    botonInicio=tkinter.Button(ventanaE,text="Inicio", width = 30, height = 15,command=lambda: opcion(2,ventanaE))
    botonInicio.grid(padx=10, pady=10,row=0,column=1)

    botonInstrucciones=tkinter.Button(ventanaE,text="Instrucciones", width = 30, height = 15,command=lambda: opcion(3,ventanaE))
    botonInstrucciones.grid(padx=10, pady=10,row=0,column=2)

    botonAtras=tkinter.Button(ventanaE,text="Atrás", width = 5, height = 2,command=lambda:opcion(4,ventanaE))
    botonAtras.grid(padx=10, pady=10,row=0,column=3)

    ventanaE.mainloop()

    return valor

def opcion(opcionEscogida,ventanaE):
    global valor
    valor = opcionEscogida
    ventanaE.destroy()


        # etiqueta= tkinter.Label(ventana, text = "hola Mundo", bg = "red")
        # side (BOTTOM, TOP), FILL= tkinter.X , fill = tkinter.Y , expand = True
        # etiqueta.pack()

        # command = lambda: saludo("Álvaro")
        # boton1=tkinter.Button(ventana, text = "Instrucciones", padx = 40 , pady = 60 , command = lambda: saludo("Álvaro"))
        # boton1.pack()
        # boton1 = tkinter.Button(ventana, text="boton 1" , width = 10, height = 5)
        # boton2 = tkinter.Button(ventana, text="boton 2", width = 10, height = 5)
        # boton3 = tkinter.Button(ventana, text="boton 3", width = 10, height = 5)
        # boton1.grid(row = 0 , column = 2)
        # boton2.grid(row=1, column=0)
        # boton3.grid(row=2, column=1)


"""
        cajaTexto = tkinter.Entry(ventana)
        cajaTexto.pack()

<<<<<<< Updated upstream
        boton1 = tkinter.Button(ventana, text= "click" , command = lambda :textoDeLaCaja(cajaTexto,etiqueta))
        boton1.pack()

        etiqueta = tkinter.Label(ventana)
        etiqueta.pack()
=======
    def saludar(self,root):
        print("¡Hey!")
        miVentana2=Ventana2(root)
>>>>>>> Stashed changes

        
        print("Esta es la ventana principal")
"""
