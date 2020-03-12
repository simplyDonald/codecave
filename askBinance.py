import urllib.request, urllib.parse, urllib.error
import json
import ssl

#api_key = 'tQNzkr*******gd8gY'
# If you have an API key, enter it here
# api_key = 'AIzaSy___IDByT70'

'''
askBinance v1.1
by Donald Abuah
Free software for real-time bitcoin price analysis and comparison with Nigerian Naira (NGN)
*Upcoming features
- Telegram bot feature
donaldabuah@gmail.com
'''


serviceurl = 'https://api.binance.com/api/v3/ticker/bookTicker?'
tickerurl = 'https://api.binance.com/api/v3/ticker/24hr?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    cryptoinput = input('Enter ticker-symbol(e.g BTCUSDT): ')
    cryptopair = cryptoinput.upper()
    if len(cryptoinput) < 1:
        cryptopair = 'BTCUSDT'


    parms = dict()
    parms['symbol'] = cryptopair
    #if api_key is not False: parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    tickerurl = tickerurl + urllib.parse.urlencode(parms)
    url2 = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCNGN'
    RATEURL = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BUSDNGN'

    print('Retrieving', url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
    except urllib.error.HTTPError:
        print('Oops!  that was no valid symbol. Can you try something else?..')
        continue


    data = uh.read().decode()
    uh2 = urllib.request.urlopen(url2, context=ctx)
    data2 = uh2.read().decode()
    th = urllib.request.urlopen(tickerurl, context=ctx)
    dataticker = th.read().decode()
    RATEURL = urllib.request.urlopen(RATEURL, context=ctx)
    RATEDATA = RATEURL.read().decode()
    print('Retrieved', len(data), 'characters')


    js = json.loads(data)
    js2 = json.loads(data2)
    js3 = json.loads(RATEDATA)
    js4 = json.loads(dataticker)


    #if 'symbol' not in js:
        #print('==== Failure To Retrieve ====')
        #print(js['message'])
        #continue


    print('+++++++++++++++++++++++++')
    #print(json.dumps(js, indent=4))

    #Calculations
    NAIRABASE = (float(js2['bidPrice']))
    CNPRICE = (float(js['askPrice']))
    EXCHNGBASE = float(js3['askPrice'])
    CNNAIRARATE = CNPRICE * EXCHNGBASE
    EXCHNG = CNNAIRARATE / CNPRICE
    TRADEEXCHNG = NAIRABASE / CNPRICE
    TRADEEXCHNG = str(round(TRADEEXCHNG,2))

    EXCHNGBASE = str(round(EXCHNGBASE,3))
    EXCHNG = str(round(EXCHNG,3))
    NAIRABASE = str(round(NAIRABASE,3))
    CNPRICE = str(round(CNPRICE,3))
    CNSYMB = (js['symbol'])
    tickdat = js4['priceChangePercent']
    tickdat = str(tickdat)
    print('+++++++++++++++++++++++++')
    print('''@@@@@@@@@@@@@@@@@@@@@@&(*,*(@@@@@@@@@
@@@@@@@@@@@@@@*,......,,,.........,@&@/////%@@@@@@
@@@@@@@@@@,.,..,,,,,,..,,#.,.,..&&&&&&&&&&//@@@@@@
@@@@@@@/......,,,,,,,,,,,,,,,.@&&..,*,.&&&&@@@@@@@
@@@@@,,..,&%(,.,,,,,,,,,,,,..&&&,,&&&&.,&&@,.#@@@@
@@@&....,,,...,..,*%,.,,,.,&@&&@&.,..,.&&&,...,@@@
@@*,,,,,,,,,,,,,,,........&@&&&&&&&&&&&@.,,.....@@
@(......,,,,,,....../////&&&@&@&@&@&&&,,,....,...@
@,......,,,,,,...,//////@&&@&/&@&&&@,...,,,,,,..,.
#.,,...,,,,,,,..,///,,////%//#&&&&//....,,,,,,,,..
,.,,..,.....,...//,,..&%//////&&////..,.,,,,,,,,,.
%.,,,,,..,,*.........&%#//#%///.////.,..,,,,,,,,.,
@,..,,,.,..,,..,,,,,&%%/%%%(.,,///..,,,,,,,...,.,.
@%...,..,.,....,,,.&%%%%&/,..*//,...,,,,,,,../&*.@
@@@@&&&&&&&/,..,..&&&&&,......,..,,.,,,,,,,..,.,@@
@@@@@&&#%%%&&&@&,..,....,.,,,,,,,,,,,,,,,,,,,,,@@@
@@@@@&@&&&&&&@&%%@@#,.,,,,,,,...*.,.,,,,,,,.,@@@@@
@@@@@@@@&@&&&%%%&&&&&@,...,,,..,*...,,,....@@@@@@@
@@@@@@@@@@@&@&%%&&&&&&@&,.,,,,,,,,,,,,,.@@@@@@@@@@
@@@@@@@@@@@@@@@&&&&&&&&&&.,.........@@@@@@@@@@@@@@
------------------TO THE MOON!!!!!----------------
    '''
    )
    print('1',CNSYMB,'=$' + CNPRICE,'\t24hr Change:' + tickdat + '%')
    print('1 BTC is also =N=' + NAIRABASE)

    if 'USDT' not in cryptopair:
        print('RATES ONLY AVAILABLE FOR USDT COIN PAIRINGS')

    elif cryptopair == 'BTCUSDT':
        print('RATE =N=' + TRADEEXCHNG,'\nBUSDNGN:=N=' + EXCHNGBASE)

    else:
        print('RATE =N=' + EXCHNG)
