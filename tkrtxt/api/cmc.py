from tkrtxt import market

def GetPrice(coin):
    coin_id = str(coin)
    procmc = market
    data = market.ticker(coin_id, convert="USD")
    coin_data = data['data'][coin_id]['quote']['USD']['price']
    return str(coin_data)

def GetPricePaired(coin, convert):
    print("PAIRD PRICE ATTEMPT")
    coin_id = str(coin)
    convert = str(convert)
    procmc = market
    data = market.ticker(coin_id, convert=convert)
    coin_data = data['data'][coin_id]['quote'][convert]['price']
    return str(coin_data)

'''

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
        c_l = c.lower()
        p_l = p.lower()
        if p_l == "":
            resp = MessagingResponse()
    # Add a text message
            coin = coinlookup[c_l]
            data = GetPrice(coin)
            resp.message(data)
            return str(resp)
        elif c_l in coinlookup:
            coin = coinlookup[c_l]
            data = GetPricePaired(coin, p_l)
            resp.message(data + " " + p.upper())
            return str(resp)
        else:
            data = GetPricePaired(c_l, p_l)
            resp.message(data + " " + p.upper())
            return str(resp)
    except:
        body = request.values.get('Body', None)
    # Start our TwiML response
        resp = MessagingResponse()
    # Add a text message
        b = body.lower()
        if b in coinlookup:
            coin = coinlookup[b]
            data = GetPrice(coin)
            resp.message(data)
            return str(resp)
        else:
            data = GetPrice(b)
            resp.message(data)
            return str(resp)


@bp.route("/sms_err", methods=['GET', 'POST'])
def sms_err():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    # body = request.values.get('Body', None)

    # Determine the right reply for this message
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    # data = body
    resp.message(" an error has occurred, please send a coin name for price in USD or a coin and currency code separated by a space")
    # resp.message(GetPrice(data, "usd") +" USD")
    return str(resp)


 
'''