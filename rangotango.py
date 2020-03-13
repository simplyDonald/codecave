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
BinanceBTCUSDT = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT'
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
uhusd = urllib.request.urlopen(BinanceBTCUSDT, context=ctx)


data1 = uh1.read().decode()
data2 = uh2.read().decode()
data3 = uh3.read().decode()
data4 = uh4.read().decode()
data5 = uh5.read().decode()
datausd = uhusd.read().decode()

print('CRUNCHING DATA...')


js1 = json.loads(data1)
js2 = json.loads(data2)
js3 = json.loads(data3)
js4 = json.loads(data4)
js5 = json.loads(data5)
js6 = json.loads(datausd)


print('+++++++++++++++++++++++++')
#print(json.dumps(js, indent=4))
#BINANCE JSON CRUNCH
BinBTCNGN = float(js1['askPrice'])
BinBTCDepth = float(js1['askQty'])
BinBIDBTCNGN = float(js1['bidPrice'])
BinBIDDepth = float(js1['bidQty'])
BinBUSDNGN = float(js2['askPrice'])
BinETHUSDT = float(js3['askPrice'])
BinETHDepth = float(js3['askQty'])
BinBIDETHUSDT = float(js3['bidQty'])
BinUSDTDAT = float(js6['askPrice'])

#BINANCE ETH Calculations
TRADEEXCHNG = BinBIDBTCNGN / BinUSDTDAT
BinETHNGN = TRADEEXCHNG * BinETHUSDT

#LUNO JSON CRUNCH
LunoBTCNGN = float(js4['asks'][0]['price'])
LunoBTCDepth = float(js4['asks'][0]['volume'])
LunoBIDBTCNGN = float(js4['bids'][0]['price'])
LunoBIDBTCDepth = float(js4['bids'][0]['volume'])
LunoETHNGN = float(js5['asks'][0]['price'])
LunoETHDepth = float(js5['asks'][0]['volume'])
LunoBIDETHNGN = float(js5['bids'][0]['price'])
LunoBIDETHDepth = float(js5['bids'][0]['volume'])


#Calculations
def percentdiff(a, b) :

    calc = int(((b - a) * 100) / a)
    result = abs(calc)

    return result

# Driver code
if __name__ == "__main__" :

    a, b = LunoBTCNGN, BinBTCNGN
    lunoBinanceBTC = percentdiff(a, b)
    if LunoBTCNGN < BinBTCNGN :
        print('**BITCOIN** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(lunoBinanceBTC) + '%')
        print( 'Luno Market BUY price:=N=' + str(LunoBTCNGN),'\nLuno Market volume:' + str(LunoBTCDepth))
        NAIRAEQ = LunoBTCNGN * LunoBTCDepth
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinBIDBTCNGN),'\nBinance Market volume:' + str(BinBIDDepth))
        BinNAIRAEQ = BinBIDBTCNGN * BinBIDDepth
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')
    elif LunoBTCNGN > BinBTCNGN:
        print('**BITCOIN** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(lunoBinanceBTC) + '%')
        print('Binance Market BUY price:=N=' + str(BinBTCNGN),'\nBinance Market volume:' + str(BinBTCDepth))
        NAIRAEQ = BinBTCNGN * BinBTCDepth
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDBTCNGN),'\nBinance Market volume:' + str(LunoBIDBTCDepth))
        BinNAIRAEQ = LunoBIDBTCNGN * LunoBIDBTCDepth
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE TRADES AT THE MOMENT')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



    a, b = LunoETHNGN, BinETHNGN
    lunoBinanceETH = percentdiff(a, b)
    if LunoETHNGN < BinETHNGN :
        print('**ETHEREUM** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(lunoBinanceETH) + '%')
        print('Luno Market BUY price:=N=' + str(LunoETHNGN),'\nLuno Market volume:' + str(LunoETHDepth))
        NAIRAEQ = LunoETHNGN * LunoETHDepth
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinETHNGN),'\nBinance Market volume:' + str(BinBIDETHUSDT))
        BinNAIRAEQ = BinETHNGN * BinBIDETHUSDT
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')
    elif LunoETHNGN > BinETHNGN:
        print('**ETHEREUM** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(lunoBinanceETH) + '%')
        print( 'Binance Market BUY price:=N=' + str(BinETHNGN),'\nBinance Market volume:' + str(BinBIDETHUSDT))
        NAIRAEQ = BinETHNGN * BinBIDETHUSDT
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDETHNGN),'\nLuno Market volume:' + str(LunoBIDETHDepth))
        BinNAIRAEQ = LunoBIDETHNGN * LunoBIDETHDepth
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE TRADES AT THE MOMENT')
