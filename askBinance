import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = 'tQNzkr*******gd8gY'
# If you have an API key, enter it here
# api_key = 'AIzaSy___IDByT70'

'''
askBinance v1.0
by Donald Abuah
Free software for real-time bitcoin price analysis and comparison with Nigerian Naira (NGN)
*Upcoming features
- Telegram bot feature
- Dynamic Ticker options
donaldabuah@gmail.com
'''


serviceurl = 'https://api.binance.com/api/v3/ticker/bookTicker'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i in range(1):
    '''
    cryptoinput = input('Enter ticker-symbol(e.g BTCUSDT): ')
    cryptopair = cryptoinput.upper()
    if len(cryptoinput) < 1: break

    parms = dict()
    parms['symbol'] = cryptopair
    #if api_key is not False: parms['key'] = api_key
    '''
    #url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', serviceurl)
    uh = urllib.request.urlopen(serviceurl, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    #try:
    #    js = json.loads(data)
    #except:
    #    js = None

    '''
        if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    '''
    js = json.loads(data)
    #print(json.dumps(js, indent=4))
    print('+++++++++++++++++++++++++')
    USD = (js[11]['askPrice'])
    CNSYMB = (js[11]['symbol'])
    print('1 BTC =$'+ USD, CNSYMB)
    #print(js[11]['symbol'])
    print('+++++++++++++++++++++++++')
    NGN = (js[651]['bidPrice'])
    CNSYMB2 = (js[651]['symbol'])
    print('1 BTC is =N=' + NGN, CNSYMB2)
    print('@@@@@@@@@@@@@@@@@@@@@@@@')
    EXCHNG = float(NGN) / float(USD)
    print('RATE =N=' + str(EXCHNG))
