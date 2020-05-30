import requests
import beepy
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


serviceurl = 'https://api.binance.com/api/v3/ticker/bookTicker'
tickerurl = 'https://api.binance.com/api/v3/ticker/24hr'

while True:

    cryptoinput = input('Enter ticker-symbol(e.g BTCUSDT): ')
    cryptopair = cryptoinput.upper()
    if len(cryptoinput) < 1:
        cryptopair = 'BTCUSDT'


    parms = dict()
    parms['symbol'] = cryptopair
    #if api_key is not False: parms['key'] = api_key

    try:
        url = requests.get('https://api.binance.com/api/v3/ticker/bookTicker', params=parms)
        tickerurl = requests.get('https://api.binance.com/api/v3/ticker/24hr', params=parms)
    except requests.exceptions.RequestException as e:
        print("====Ooops..seems there's a connection error====\n",e)
        beepy.beep(sound='error')
        continue

    url2 = requests.get('https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCNGN')
    RATEURL = requests.get('https://api.binance.com/api/v3/ticker/bookTicker?symbol=BUSDNGN')

    print('Retrieving', url.url)

    js = url.json()
    js2 = url2.json()
    js3 = RATEURL.json()
    js4 = tickerurl.json()


    if 'symbol' not in js:
        print('==== Oops! there was a glitch somewhere... ====')
        print(js['msg'])
        beepy.beep(sound='error')
        continue

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

    #String conversions + json extraction
    CNNAIRARATE = str(round(CNNAIRARATE,2))
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
        print('RATE =N=' + EXCHNG, '\nNAIRA EQ.:=N=' + CNNAIRARATE)
    beepy.beep(sound='ping')
