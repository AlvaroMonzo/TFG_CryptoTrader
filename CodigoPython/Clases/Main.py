from CodigoPython.Clases import VentanaLogin

if __name__ == "__main__":

    try:

        VentanaLogin.VentanaLogin()
    except Exception as e:
        print(e)

# numero=1
# hilo = HiloOperacion.MiHilo(args=(numero,numero*numero), daemon=False)
# hilo.start()
