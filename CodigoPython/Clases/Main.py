from CodigoPython.Clases import VentanaLogin
from CodigoPython.Clases import VentanaCarga
from CodigoPython.Clases import VentanaEleccion
from CodigoPython.Clases import HiloOperacion

if __name__ == "__main__":

    try:

        VentanaLogin.VentanaLogin()
    except Exception as e:
        print(e)

# numero=1
# hilo = HiloOperacion.MiHilo(args=(numero,numero*numero), daemon=False)
# hilo.start()
