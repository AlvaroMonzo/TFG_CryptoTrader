from requests import Request,Session
import time

url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers={
    'Accepts': 'application/json',
    'X-CMC_Basic_APY_KEY': '334a6f24-17e0-4efb-ab4d-7033e75af5fd'

}
params={
    'slug': 'bitcoin',
    'convert': 'USD'
}

session=Session()
session.headers.update(headers)

response= session.get(url,params=params)

print(response)
#json=requests.get(url,params=params,headers=headers).json()


