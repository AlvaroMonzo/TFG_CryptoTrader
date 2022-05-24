from CodigoPython.Clases import VentanaLogin
from CodigoPython.Clases import VentanaCarga
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import HiloOperacion


if __name__ == "__main__":

    try:
        VentanaLogin.VentanaLogin()
    except:
        print("Fallo de cierre")



hilo = HiloOperacion.MiHilo()
hilo.start()
