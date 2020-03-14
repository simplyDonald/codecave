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
bin_Api_BTCNGN = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCNGN'
bin_Api_BUSDNGN = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BUSDNGN'
bin_Api_ETHBUSD = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=ETHBUSD'
luno_Api_BTCNGN = 'https://api.mybitx.com/api/1/orderbook?pair=XBTNGN'
luno_Api_ETHNGN = 'https://api.mybitx.com/api/1/orderbook?pair=ETHNGN'


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

uh1 = urllib.request.urlopen(bin_Api_BTCNGN, context=ctx)
uh2 = urllib.request.urlopen(bin_Api_BUSDNGN, context=ctx)
uh3 = urllib.request.urlopen(bin_Api_ETHBUSD, context=ctx)
uh4 = urllib.request.urlopen(luno_Api_BTCNGN, context=ctx)
uh5 = urllib.request.urlopen(luno_Api_ETHNGN, context=ctx)



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
bin_Ask_BTCNGN = float(js1['askPrice'])
bin_Ask_BTCNGN_Depth = float(js1['askQty'])
bin_Bid_BTCNGN = float(js1['bidPrice'])
bin_Bid_BTCNGN_Depth = float(js1['bidQty'])
bin_Ask_BUSDNGN = float(js2['askPrice'])
bin_Ask_BUSDNGN_Depth = float(js2['askQty'])
bin_Bid_BUSDNGN = float(js2['bidPrice'])
bin_Bid_BUSDNGN_Depth = float(js2['bidQty'])
bin_Ask_ETHBUSD = float(js3['askPrice'])
bin_Ask_ETHBUSD_Depth = float(js3['askQty'])
bin_Bid_ETHBUSD = float(js3['bidPrice'])
bin_Bid_ETHBUSD_Depth = float(js3['bidQty'])

#BINANCE ETH Calculations

bin_Ask_ETHNGN = bin_Ask_ETHBUSD * bin_Ask_BUSDNGN
bin_Bid_ETHNGN = bin_Bid_ETHBUSD * bin_Bid_BUSDNGN

#LUNO JSON CRUNCH
luno_Ask_BTCNGN = float(js4['asks'][0]['price'])
luno_Ask_BTCNGN_Depth = float(js4['asks'][0]['volume'])
luno_Bid_BTCNGN = float(js4['bids'][0]['price'])
luno_Bid_BTCNGN_Depth = float(js4['bids'][0]['volume'])
luno_Ask_ETHNGN = float(js5['asks'][0]['price'])
luno_Ask_ETHNGN_Depth = float(js5['asks'][0]['volume'])
luno_Bid_ETHNGN = float(js5['bids'][0]['price'])
luno_Bid_ETHNGN_Depth = float(js5['bids'][0]['volume'])


#Calculations
def percentdiff(a, b) :

    calc = int(((b - a) * 100) / a)
    result = abs(calc)

    return result

# Driver code
if __name__ == "__main__" :

<<<<<<< HEAD
    if luno_Ask_BTCNGN < bin_Bid_BTCNGN :
        a, b = luno_Ask_BTCNGN, bin_Bid_BTCNGN
=======
    if LunoBTCNGN < BinBIDBTCNGN :
        a, b = LunoBTCNGN, BinBIDBTCNGN
>>>>>>> c720f80ecbf981d58482dc1730ee9a03c94e972e
        Delta = percentdiff(a, b)

        print('**BITCOIN** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(Delta) + '%')
<<<<<<< HEAD
        print( 'Luno Market BUY price:=N=' + str(luno_Ask_BTCNGN),'\nLuno Market volume:' + str(luno_Ask_BTCNGN_Depth))
        naira_Eq1= round(luno_Ask_BTCNGN * luno_Ask_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Binance Market SELL price:=N=' + str(bin_Bid_BTCNGN),'\nBinance Market volume:' + str(bin_Bid_BTCNGN_Depth))
        naira_Eq2 = round(bin_Bid_BTCNGN * bin_Bid_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = (Delta * naira_Eq1) - (0.014 * naira_Eq1)
=======
        print( 'Luno Market BUY price:=N=' + str(LunoBTCNGN),'\nLuno Market volume:' + str(LunoBTCDepth))
        NAIRAEQ = round(LunoBTCNGN * LunoBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinBIDBTCNGN),'\nBinance Market volume:' + str(BinBIDDepth))
        BinNAIRAEQ = round(BinBIDBTCNGN * BinBIDDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = (Delta * NAIRAEQ) - (0.014 * NAIRAEQ)
>>>>>>> c720f80ecbf981d58482dc1730ee9a03c94e972e
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')


<<<<<<< HEAD
    elif bin_Ask_BTCNGN < luno_Bid_BTCNGN:
        a, b = bin_Ask_BTCNGN, luno_Bid_BTCNGN
        Delta = percentdiff(a, b)
        print('**BITCOIN** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Binance Market BUY price:=N=' + str(bin_Ask_BTCNGN),'\nBinance Market volume:' + str(bin_Ask_BTCNGN_Depth))
        naira_Eq1 = round(bin_Ask_BTCNGN * bin_Ask_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Luno Market SELL price:=N=' + str(luno_Bid_BTCNGN),'\nLuno Market volume:' + str(luno_Bid_BTCNGN_Depth))
        naira_Eq2 = round(luno_Bid_BTCNGN * luno_Bid_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = Delta * (naira_Eq1 - 150)
=======
    elif BinBTCNGN < LunoBIDBTCNGN:
        a, b = BinBTCNGN, LunoBIDBTCNGN
        Delta = percentdiff(a, b)
        print('**BITCOIN** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Binance Market BUY price:=N=' + str(BinBTCNGN),'\nBinance Market volume:' + str(BinBTCDepth))
        NAIRAEQ = round(BinBTCNGN * BinBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDBTCNGN),'\nLuno Market volume:' + str(LunoBIDBTCDepth))
        BinNAIRAEQ = round(LunoBIDBTCNGN * LunoBIDBTCDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = Delta * (NAIRAEQ - 150)
>>>>>>> c720f80ecbf981d58482dc1730ee9a03c94e972e
        profit_after_trade = (profit_after_deposit * 0.00075)
        print('PROFIT P/DEPO(Bank Transfer):~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE BITCOIN TRADES AT THE MOMENT')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


<<<<<<< HEAD
    if luno_Ask_ETHNGN < bin_Bid_ETHNGN :
        a, b = luno_Ask_ETHNGN, bin_Bid_ETHNGN
        Delta = percentdiff(a, b)
        print('**ETHEREUM** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Luno Market BUY price:=N=' + str(luno_Ask_ETHNGN),'\nLuno Market volume:' + str(luno_Ask_ETHNGN_Depth))
        naira_Eq1 = round(luno_Ask_ETHNGN * luno_Ask_ETHNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Binance Market SELL price:=N=' + str(bin_Bid_ETHNGN),'\nBinance Market volume:' + str(bin_Bid_ETHBUSD_Depth))
        naira_EQ2 = round(bin_Bid_ETHNGN * bin_Bid_ETHBUSD,2)
        print('NAIRAEQ.:=N=' + str(naira_EQ2))
        profit_after_deposit = (Delta * naira_Eq1) - (0.014 * naira_Eq1)
=======

    a, b = LunoETHNGN, BinBIDETHNGN
    Delta = percentdiff(a, b)
    if LunoETHNGN < BinBIDETHNGN :
        print('**ETHEREUM** \nLUNO:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Luno Market BUY price:=N=' + str(LunoETHNGN),'\nLuno Market volume:' + str(LunoETHDepth))
        NAIRAEQ = round(LunoETHNGN * LunoETHDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Binance Market SELL price:=N=' + str(BinBIDETHNGN),'\nBinance Market volume:' + str(BinBIDDepthETHUSDT))
        BinNAIRAEQ = round(BinETHNGN * BinBIDETHUSDT,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = (Delta * NAIRAEQ) - (0.014 * NAIRAEQ)
>>>>>>> c720f80ecbf981d58482dc1730ee9a03c94e972e
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')

    elif bin_Ask_ETHNGN < luno_Bid_ETHNGN:

<<<<<<< HEAD
        a, b = bin_Ask_ETHNGN, luno_Bid_ETHNGN
        Delta = percentdiff(a, b)
        print('**ETHEREUM** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(Delta) + '%')
        print( 'Binance Market BUY price:=N=' + str(bin_Ask_ETHNGN),'\nBinance Market volume:' + str(bin_Ask_ETHBUSD_Depth))
        naira_Eq1 = round(bin_Ask_ETHNGN * bin_Ask_ETHBUSD_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Luno Market SELL price:=N=' + str(luno_Bid_ETHNGN),'\nLuno Market volume:' + str(luno_Bid_ETHNGN_Depth))
        naira_Eq2 = round(luno_Bid_ETHNGN * luno_Bid_ETHNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = Delta * (naira_Eq1 - 150)
=======
        a, b = BinETHNGN, LunoBIDETHNGN
        Delta = percentdiff(a, b)
        print('**ETHEREUM** \nBINANCE:BUY ===> \tLUNO:SELL')
        print('Delta:' + str(Delta) + '%')
        print( 'Binance Market BUY price:=N=' + str(BinETHNGN),'\nBinance Market volume:' + str(BinETHDepth))
        NAIRAEQ = round(BinETHNGN * BinETHDepth,2)
        print('NAIRAEQ.:=N=' + str(NAIRAEQ),'\n--------')
        print('Luno Market SELL price:=N=' + str(LunoBIDETHNGN),'\nLuno Market volume:' + str(LunoBIDETHDepth))
        BinNAIRAEQ = round(LunoBIDETHNGN * LunoBIDETHDepth,2)
        print('NAIRAEQ.:=N=' + str(BinNAIRAEQ))
        profit_after_deposit = Delta * (NAIRAEQ - 150)
>>>>>>> c720f80ecbf981d58482dc1730ee9a03c94e972e
        profit_after_trade = (profit_after_deposit * 0.00075)
        print('PROFIT P/DEPO(Bank Transfer):~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE ETHEREUM TRADES AT THE MOMENT')
