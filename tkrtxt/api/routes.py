from flask import request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from tkrtxt.api.cmc import GetPrice, GetPricePaired
from tkrtxt.api import bp
from flask import send_file

@bp.route('/get_lander')
def get_lander():
    filename = 'static/images/lander.jpg'
    return send_file(filename, mimetype='image/gif')

coinlookup = {'ada': 'cardano',
  'ae': 'aeternity',
  'aion': 'aion',
  'ardr': 'ardor',
  'ark': 'ark',
  'bat': 'basic-attention-token',
  'bcc': 'bitconnect',
  'bch': 'bitcoin-cash',
  'bcn': 'bytecoin',
  'bnb': 'binance-coin',
  'bnt': 'bancor',
  'btc': 'bitcoin',
  'btcd': 'bitcoindark',
  'btg': 'bitcoin-gold',
  'btm': 'bytom',
  'bts': 'bitshares',
  'cvc': 'civic',
  'dash': 'dash',
  'dbc': 'deepbrain-chain',
  'dcn': 'dentacoin',
  'dcr': 'decred',
  'dent': 'dent',
  'dgb': 'digibyte',
  'dgd': 'digixdao',
  'doge': 'dogecoin',
  'drgn': 'dragonchain',
  'elf': 'aelf',
  'eng': 'enigma',
  'eos': 'eos',
  'etc': 'ethereum-classic',
  'eth': 'ethereum',
  'ethos': 'ethos',
  'etn': 'electroneum',
  'fct': 'factom',
  'fun': 'funfair',
  'gas': 'gas',
  'gbyte': 'byteball-bytes',
  'gno': 'gnosis',
  'gnt': 'golem',
  'hsr': 'hshare',
  'icn': 'iconomi',
  'icx': 'icon',
  'kcs': 'kucoin-shares',
  'kin': 'kin',
  'kmd': 'komodo',
  'knc': 'kyber-network',
  'link': 'chainlink',
  'lsk': 'lisk',
  'ltc': 'litecoin',
  'maid': 'maidsafecoin',
  'miota': 'iota',
  'mona': 'monacoin',
  'nebl': 'neblio',
  'neo': 'neo',
  'nxs': 'nexus',
  'nxt': 'nxt',
  'omg': 'omisego',
  'pac': 'paccoin',
  'pay': 'tenx',
  'pivx': 'pivx',
  'poe': 'poet',
  'powr': 'power-ledger',
  'ppt': 'populous',
  'qash': 'qash',
  'qsp': 'quantstamp',
  'qtum': 'qtum',
  'rdd': 'reddcoin',
  'rdn': 'raiden-network-token',
  'rep': 'augur',
  'req': 'request-network',
  'rhoc': 'rchain',
  'salt': 'salt',
  'san': 'santiment network token',
  'sc': 'siacoin',
  'snt': 'status',
  'steem': 'steem',
  'strat': 'stratis',
  'sub': 'substratum',
  'sys': 'syscoin',
  'tnb': 'time-new-bank',
  'trx': 'tron',
  'usdt': 'tether',
  'ven': 'vechain',
  'veri': 'veritaseum',
  'waves': 'waves',
  'wax': 'wax',
  'wtc': 'walton',
  'xdn': 'digitalnote',
  'xem': 'nem',
  'xlm': 'stellar',
  'xmr': 'monero',
  'xp': 'experience-points',
  'xrb': 'raiblocks',
  'xrp': 'ripple',
  'xvg': 'verge',
  'xzc': 'zcoin',
  'zcl': 'zclassic',
  'zec': 'zcash',
  'zrx': '0x'}



@bp.route("/test", methods=['GET', 'POST'])
def test_cmc():
    data = GetPrice("XMR")
    print(f"Data: {data}")
    return jsonify({'Coin Data': data})

    # Twilio Crypto Response
@bp.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number


    try:
        body = request.values.get('Body', None)
    # Start our TwiML response
        resp = MessagingResponse()
    # Split incoming tkr and pair
        c, p = body.split(" ")
        coin_upper = c.upper()
        pair_upper = p.upper()
        print(f"COIN: {coin_upper} PAIR: {pair_upper}")
        if pair_upper == "":
            data = GetPrice(coin_upper)
            resp.message(data)
            return str(resp)
        else:
            print("ATTEMOTING PRICED PAIR")
            data = GetPricePaired(coin_upper, pair_upper)
            resp.message(data + " " + pair_upper)
            return str(resp)
    except:
        print("Ghost Exception")

    try:       
        body = request.values.get('Body', None)
    # Start our TwiML response
        resp = MessagingResponse()
    # Add a text message
        b = body.upper()
        data = GetPrice(b)
        resp.message(data)
        return str(resp)

    except:
        return "Failed request"

