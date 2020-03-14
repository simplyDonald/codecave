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
BinBIDETHUSDT = float(js3['bidPrice'])
BinBIDDepthETHUSDT = float(js3['bidQty'])
BinUSDTDAT = float(js6['askPrice'])

#BINANCE ETH Calculations
TRADEEXCHNG = BinBIDBTCNGN / BinUSDTDAT
BinETHNGN = TRADEEXCHNG * BinETHUSDT
BinBIDETHNGN = TRADEEXCHNG * BinBIDETHUSDT

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

    if LunoBTCNGN < BinBIDBTCNGN :
        a, b = LunoBTCNGN, BinBIDBTCNGN
        lunoBinanceBTC = percentdiff(a, b)

        print('**BITCOIN** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(lunoBinanceBTC) + '%')
        print( 'Luno Market BUY price:=N=' + str(LunoBTCNGN),'\nLuno Market volume:' + str(LunoBTCDepth))
        NAIRAEQ = round(LunoBTCNGN * LunoBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinBIDBTCNGN),'\nBinance Market volume:' + str(BinBIDDepth))
        BinNAIRAEQ = round(BinBIDBTCNGN * BinBIDDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = (lunoBinanceBTC * NAIRAEQ) - (0.014 * NAIRAEQ)
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')


    elif BinBTCNGN < LunoBIDBTCNGN:
        a, b = BinBTCNGN, LunoBIDBTCNGN
        lunoBinanceBTC = percentdiff(a, b)
        print('**BITCOIN** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(lunoBinanceBTC) + '%')
        print('Binance Market BUY price:=N=' + str(BinBTCNGN),'\nBinance Market volume:' + str(BinBTCDepth))
        NAIRAEQ = round(BinBTCNGN * BinBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDBTCNGN),'\nLuno Market volume:' + str(LunoBIDBTCDepth))
        BinNAIRAEQ = round(LunoBIDBTCNGN * LunoBIDBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = lunoBinanceETH * (NAIRAEQ - 150)
        profit_after_trade = (profit_after_deposit * 0.00075)
        print('PROFIT P/DEPO(Bank Transfer):~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE BITCOIN TRADES AT THE MOMENT')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



    a, b = LunoETHNGN, BinBIDETHNGN
    lunoBinanceETH = percentdiff(a, b)
    if LunoETHNGN < BinBIDETHNGN :
        print('**ETHEREUM** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(lunoBinanceETH) + '%')
        print('Luno Market BUY price:=N=' + str(LunoETHNGN),'\nLuno Market volume:' + str(LunoETHDepth))
        NAIRAEQ = round(LunoETHNGN * LunoETHDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinBIDETHNGN),'\nBinance Market volume:' + str(BinBIDDepthETHUSDT))
        BinNAIRAEQ = round(BinETHNGN * BinBIDETHUSDT,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = (lunoBinanceETH * NAIRAEQ) - (0.014 * NAIRAEQ)
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')

    elif BinETHNGN < LunoBIDETHNGN:

        a, b = BinETHNGN, LunoBIDETHNGN
        lunoBinanceETH = percentdiff(a, b)
        print('**ETHEREUM** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(lunoBinanceETH) + '%')
        print( 'Binance Market BUY price:=N=' + str(BinETHNGN),'\nBinance Market volume:' + str(BinETHDepth))
        NAIRAEQ = round(BinETHNGN * BinETHDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDETHNGN),'\nLuno Market volume:' + str(LunoBIDETHDepth))
        BinNAIRAEQ = round(LunoBIDETHNGN * LunoBIDETHDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = lunoBinanceETH * (NAIRAEQ - 150)
        profit_after_trade = (profit_after_deposit * 0.00075)
        print('PROFIT P/DEPO(Bank Transfer):~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if NAIRAEQ > BinNAIRAEQ:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE ETHEREUM TRADES AT THE MOMENT')
