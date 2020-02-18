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


# Ignore SSL certificate errors
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

    url = serviceurl + urllib.parse.urlencode(parms)
    url2 = 'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCNGN'

    print('Retrieving', url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
    except urllib.error.HTTPError:
        print('Oops!  that was no valid symbol. Can you try something else?..')
        continue


    data = uh.read().decode()
    uh2 = urllib.request.urlopen(url2, context=ctx)
    data2 = uh2.read().decode()
    print('Retrieved', len(data), 'characters')


    js = json.loads(data)
    js2 = json.loads(data2)


    #if 'symbol' not in js:
        #print('==== Failure To Retrieve ====')
        #print(js['message'])
        #continue


    print('+++++++++++++++++++++++++')
    #print(json.dumps(js, indent=4))

    #Calculations
    NAIRABASE = (float(js2['bidPrice']))
    CNPRICE = (float(js['askPrice']))
    EXCHNG = NAIRABASE / CNPRICE

    EXCHNG = str(round(EXCHNG,3))
    NAIRABASE = str(round(NAIRABASE,3))
    CNPRICE = str(round(CNPRICE,3))
    CNSYMB = (js['symbol'])
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
    print('1',CNSYMB,'=$' + CNPRICE)
    print('1 BTC is also =N=' + NAIRABASE)

    if cryptopair == 'BTCUSDT':
        print('RATE =N=' + EXCHNG)
    else:
        print('RATE = UNAVAILABLE')
