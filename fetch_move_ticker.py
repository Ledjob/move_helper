# Python

import ccxt as ccxt
import requests

rest =  'https://ftx.com/api'
future_name = 'BTC-MOVE-0516'
stats =f'/futures/{future_name}/stats'

def print_stats():

    url = rest + stats
#url = 'https://ftx.com/api/futures/btc-move-0414/stats'
    response = requests.get(url)
    print(response.json())


def print_ftx_move_ticker():
    ftx = ccxt.ftx()
    ticker = ftx.fetch_ticker(future_name)
    required_fields = ["datetime", "open", "close", "change", "percentage"]
    required_fields2 = ['name', 'last', 'bid', 'ask', 'last', 'change1h', 'change24h', 'changeBod', 'priceHigh24h', 'priceLow24h']
    dict_info = {key:value for key, value in ticker['info'].items() if key in required_fields2}
    dict2 = {key:value for key, value in ticker.items() if key in required_fields}
    #print(ftx.fetch_ticker('BTC-MOVE-0414'))
    print(dict2)
    print(dict_info)

if __name__ == '__main__':

    print_ftx_move_ticker()
    print_stats()
