from CodigoPython.InterfazGrafica import Interfaz
from binance.client import Client

client=Interfaz.ventanaLogin()

Interfaz.ventanaEleccion(client)


btc_balance = client.get_asset_balance(asset='BTC')
print("Balance: {}".format(btc_balance))

print("Error en la app")


