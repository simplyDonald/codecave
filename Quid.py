import requests
import json




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
Quid_Api_BTCNGN = 'https://www.quidax.com/api/v1/markets/btcngn/depth?limit=1'
Quid_Api_ETHNGN = 'https://www.quidax.com/api/v1/markets/ethngn/depth?limit=1'


'''# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


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

uh1 = requests.get(bin_Api_BTCNGN)
uh2 = requests.get(bin_Api_BUSDNGN)
uh3 = requests.get(bin_Api_ETHBUSD)
uh4 = requests.get(Quid_Api_BTCNGN)
uh5 = requests.get(Quid_Api_ETHNGN)



data1 = uh1.json()
data2 = uh2.json()
data3 = uh3.json()
data4 = uh4.json()
data5 = uh5.json()

print('CRUNCHING DATA...')



print('+++++++++++++++++++++++++')
#print(json.dumps(js, indent=4))
#BINANCE JSON CRUNCH
bin_Ask_BTCNGN = float(data1['askPrice'])
bin_Ask_BTCNGN_Depth = float(data1['askQty'])
bin_Bid_BTCNGN = float(data1['bidPrice'])
bin_Bid_BTCNGN_Depth = float(data1['bidQty'])
bin_Ask_BUSDNGN = float(data2['askPrice'])
bin_Ask_BUSDNGN_Depth = float(data2['askQty'])
bin_Bid_BUSDNGN = float(data2['bidPrice'])
bin_Bid_BUSDNGN_Depth = float(data2['bidQty'])
bin_Ask_ETHBUSD = float(data3['askPrice'])
bin_Ask_ETHBUSD_Depth = float(data3['askQty'])
bin_Bid_ETHBUSD = float(data3['bidPrice'])
bin_Bid_ETHBUSD_Depth = float(data3['bidQty'])

#BINANCE ETH Calculations

bin_Ask_ETHNGN = bin_Ask_ETHBUSD * bin_Ask_BUSDNGN
bin_Bid_ETHNGN = bin_Bid_ETHBUSD * bin_Bid_BUSDNGN

#Quid JSON CRUNCH
Quid_Ask_BTCNGN = float(data4['data']['asks'][0][0])
Quid_Ask_BTCNGN_Depth = float(data4['data']['asks'][0][1])
Quid_Bid_BTCNGN = float(data4['data']['bids'][0][0])
Quid_Bid_BTCNGN_Depth = float(data4['data']['bids'][0][1])
Quid_Ask_ETHNGN = float(data5['data']['asks'][0][0])
Quid_Ask_ETHNGN_Depth = float(data5['data']['asks'][0][1])
Quid_Bid_ETHNGN = float(data5['data']['bids'][0][0])
Quid_Bid_ETHNGN_Depth = float(data5['data']['bids'][0][1])

#Calculations
def percentdiff(a, b) :

    calc = int(((b - a) * 100) / a)
    result = abs(calc)

    return result

# Driver code
if __name__ == "__main__" :

    if Quid_Ask_BTCNGN < bin_Bid_BTCNGN :
        a, b = Quid_Ask_BTCNGN, bin_Bid_BTCNGN
        Delta = percentdiff(a, b)

        print('**BITCOIN** \nQuid:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(Delta) + '%')
        print( 'Quid Market BUY price:=N=' + str(Quid_Ask_BTCNGN),'\nQuid Market volume:' + str(Quid_Ask_BTCNGN_Depth))
        naira_Eq1= round(Quid_Ask_BTCNGN * Quid_Ask_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Binance Market SELL price:=N=' + str(bin_Bid_BTCNGN),'\nBinance Market volume:' + str(bin_Bid_BTCNGN_Depth))
        naira_Eq2 = round(bin_Bid_BTCNGN * bin_Bid_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = (Delta * naira_Eq1) - (0.014 * naira_Eq1)
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
            print('BALANCED TRADE')

    elif bin_Ask_BTCNGN < Quid_Bid_BTCNGN:
        a, b = bin_Ask_BTCNGN, Quid_Bid_BTCNGN
        Delta = percentdiff(a, b)
        print('**BITCOIN** \nBINANCE:BUY ===> \tQuid:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Binance Market BUY price:=N=' + str(bin_Ask_BTCNGN),'\nBinance Market volume:' + str(bin_Ask_BTCNGN_Depth))
        naira_Eq1 = round(bin_Ask_BTCNGN * bin_Ask_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Quid Market SELL price:=N=' + str(Quid_Bid_BTCNGN),'\nQuid Market volume:' + str(Quid_Bid_BTCNGN_Depth))
        naira_Eq2 = round(Quid_Bid_BTCNGN * Quid_Bid_BTCNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = Delta * (naira_Eq1 - 150)
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


    if Quid_Ask_ETHNGN < bin_Bid_ETHNGN :
        a, b = Quid_Ask_ETHNGN, bin_Bid_ETHNGN
        Delta = percentdiff(a, b)
        print('**ETHEREUM** \nQuid:BUY ===> \tBINANCE:SELL')
        print('Delta:' + str(Delta) + '%')
        print('Quid Market BUY price:=N=' + str(Quid_Ask_ETHNGN),'\nQuid Market volume:' + str(Quid_Ask_ETHNGN_Depth))
        naira_Eq1 = round(Quid_Ask_ETHNGN * Quid_Ask_ETHNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Binance Market SELL price:=N=' + str(bin_Bid_ETHNGN),'\nBinance Market volume:' + str(bin_Bid_ETHBUSD_Depth))
        naira_Eq2 = round(bin_Bid_ETHNGN * bin_Bid_ETHBUSD_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = (Delta * naira_Eq1) - (0.014 * naira_Eq1)
        profit_after_trade = (profit_after_deposit * 0.01)
        print('PROFIT P/DEPO:~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')

    elif bin_Ask_ETHNGN < Quid_Bid_ETHNGN:
        a, b = bin_Ask_ETHNGN, Quid_Bid_ETHNGN
        Delta = percentdiff(a, b)
        print('**ETHEREUM** \nBINANCE:BUY ===> \tQuid:SELL')
        print('Delta:' + str(Delta) + '%')
        print( 'Binance Market BUY price:=N=' + str(bin_Ask_ETHNGN),'\nBinance Market volume:' + str(bin_Ask_ETHBUSD_Depth))
        naira_Eq1 = round(bin_Ask_ETHNGN * bin_Ask_ETHBUSD_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq1),'\n--------')
        print('Quid Market SELL price:=N=' + str(Quid_Bid_ETHNGN),'\nQuid Market volume:' + str(Quid_Bid_ETHNGN_Depth))
        naira_Eq2 = round(Quid_Bid_ETHNGN * Quid_Bid_ETHNGN_Depth,2)
        print('NAIRAEQ.:=N=' + str(naira_Eq2))
        profit_after_deposit = Delta * (naira_Eq1 - 150)
        profit_after_trade = (profit_after_deposit * 0.00075)
        print('PROFIT P/DEPO(Bank Transfer):~ =N=' + str(profit_after_deposit))
        print('PROFIT P/TRADE:~ =N=' + str(profit_after_trade))
        if naira_Eq1 > naira_Eq2:
            print('DEFICIT ON TRADE')
        else:
                print('BALANCED TRADE')
    else:
        print('EQUIVALENT PRICES: NO PROFITABLE ETHEREUM TRADES AT THE MOMENT')
