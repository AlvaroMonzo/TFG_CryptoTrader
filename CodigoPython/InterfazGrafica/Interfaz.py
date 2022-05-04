import tkinter


def ventanaLogin():
        ventana=tkinter.Tk()
        ventana.geometry("1000x1000")
        #etiqueta= tkinter.Label(ventana, text = "hola Mundo", bg = "red")
        #side (BOTTOM, TOP), FILL= tkinter.X , fill = tkinter.Y , expand = True
        #etiqueta.pack()

        #command = lambda: saludo("Álvaro")
        #boton1=tkinter.Button(ventana, text = "Instrucciones", padx = 40 , pady = 60 , command = lambda: saludo("Álvaro"))
        #boton1.pack()
        #boton1 = tkinter.Button(ventana, text="boton 1" , width = 10, height = 5)
        #boton2 = tkinter.Button(ventana, text="boton 2", width = 10, height = 5)
        #boton3 = tkinter.Button(ventana, text="boton 3", width = 10, height = 5)
        #boton1.grid(row = 0 , column = 2)
        #boton2.grid(row=1, column=0)
        #boton3.grid(row=2, column=1)


        #ventana.mainloop()

"""
        cajaTexto = tkinter.Entry(ventana)
        cajaTexto.pack()

        boton1 = tkinter.Button(ventana, text= "click" , command = lambda :textoDeLaCaja(cajaTexto,etiqueta))
        boton1.pack()

        etiqueta = tkinter.Label(ventana)
        etiqueta.pack()

        
        print("Esta es la ventana principal")
"""



def saludo (nombre):
        print("hola bb" + nombre)

def textoDeLaCaja(cajaTexto,etiqueta):
        textoCaja= cajaTexto.get()
        etiqueta["text"] = textoCaja
        print(textoCaja)