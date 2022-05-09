from CodigoPython.InterfazGrafica import Interfaz
from binance.client import Client

client = Interfaz.ventanaLogin()
opcion = ""
try:
    btc_balance = client.get_asset_balance(asset='BTC')
    print("Balance: {}".format(btc_balance))
    opcion = Interfaz.ventanaEleccion(client)
except:
    print("Error en la app")

if opcion == 1:
    print("Opcion 1")
elif opcion == 2:
    print("Opcion 2")
elif opcion == 3:
    print("Opcion 3")
elif opcion == 4:
    client=Interfaz.ventanaLogin()
else:
    print("Fallo en la APP")


