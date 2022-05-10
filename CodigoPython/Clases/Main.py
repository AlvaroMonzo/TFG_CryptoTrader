from CodigoPython.Clases import VentanaLogin
from CodigoPython.Clases import VentanaCarga
from CodigoPython.Clases import VentanaEleccion

if __name__ == "__main__":

    try:
        VentanaLogin.VentanaLogin()
    except:
        print("Fallo de cierre")
