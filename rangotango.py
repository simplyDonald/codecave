import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = 'tQNzkr*******gd8gY'
# If you have an API key, enter it here
# api_key = 'AIzaSy___IDByT70'

'''
RANGOTANGO v1.0
by Donald Abuah & Victor Elisha
Proprietary software for real-time Arb with Nigerian Naira (NGN)

donaldabuah@gmail.com
'''

#Queries URL
BinanceBTCNGN = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCNGN'
BinanceBUSDNGN = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BUSDNGN'
BinanceETHUSDT = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=ETHUSDT'
LunoBTCNGN = 'https://api.mybitx.com/api/1/orderbook?pair=XBTNGN'
LunoETHNGN = 'https://api.mybitx.com/api/1/orderbook?pair=ETHNGN'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''

while True:

cryptoinput = input('Enter ticker-symbol(e.g BTCUSDT): ')
cryptopair = cryptoinput.upper()
if len(cryptoinput) < 1:
    print('There\'s so much SPACE between us,',end ='')
    print(' please input a value :)')
    continue



parms = dict()
parms['symbol'] = cryptopair
#if api_key is not False: parms['key'] = api_key
'''


print('LOADING.....')

uh1 = urllib.request.urlopen(BinanceBTCNGN, context=ctx)
uh2 = urllib.request.urlopen(BinanceBUSDNGN, context=ctx)
uh3 = urllib.request.urlopen(BinanceETHUSDT, context=ctx)
uh4 = urllib.request.urlopen(LunoBTCNGN, context=ctx)
uh5 = urllib.request.urlopen(LunoETHNGN, context=ctx)


data1 = uh1.read().decode()
data2 = uh2.read().decode()
data3 = uh3.read().decode()
data4 = uh4.read().decode()
data5 = uh5.read().decode()

print('CRUNCHING DATA...')


js1 = json.loads(data1)
js2 = json.loads(data2)
js3 = json.loads(data3)
js4 = json.loads(data4)
js5 = json.loads(data5)


print('+++++++++++++++++++++++++')
#print(json.dumps(js, indent=4))
#BINANCE JSON CRUNCH
BinBTCNGN = float(js1['askPrice'])
BinBTCDepth = float(js1['askQty'])
BinBUSDNGN = float(js2['askPrice'])
BinETHUSDT = float(js3['askPrice'])
BinETHDepth = float(js3['askQty'])

#BINANCE ETH Calculations
BinETHNGN = BinBUSDNGN * BinETHUSDT

#LUNO JSON CRUNCH
LunoBTCNGN = float(js4['asks'][0]['price'])
LunoBTCDepth = float(js4['asks'][0]['volume'])
LunoETHNGN = float(js5['asks'][0]['price'])
LunoETHDepth = float(js5['asks'][0]['volume'])


#Calculations
def percentdiff(a, b) :

    calc = int(((b - a) * 100) / a)
    result = abs(calc)

    return result

# Driver code
if __name__ == "__main__" :

    a, b = LunoBTCNGN, BinBTCNGN
    lunoBinanceBTC = percentdiff(a, b)
    print('Arb-BITCOIN LUNO-BINANCE ==> '+ str(lunoBinanceBTC) + '%')

    a, b = LunoETHNGN, BinETHNGN
    lunoBinanceETH = percentdiff(a, b)
    print('Arb-ETHEREUM LUNO-BINANCE ==> '+ str(lunoBinanceETH) + '%')
