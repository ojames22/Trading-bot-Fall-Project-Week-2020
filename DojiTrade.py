import ssl
import websocket, json
import requests


API_Key = "PKRJJ2QQ0IU0TXNKXFCU"
Secret_Key = "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm"

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_Key, 'APCA-API-SECRET-KEY': Secret_Key}

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": API_Key, "secret_key": Secret_Key}
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "listen", "data": {"streams": ["AM.TSLA"]}}

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("Received a message")
    print(message)

    print("Checking for vw in stream...")
    price_dict = json.loads(message)

    #{"stream":"listening","data":{"streams":["AM.TSLA"]}}
    #if "stream" in price_dict["stream"]["listening"]["data"]:
    #    price = price_dict["data"]["vw"]

    #{"stream":"listening","data":{"streams":["AM.TSLA"]}}
    #"stream":"AM.TSLA","data":{"ev":"AM","T":"TSLA","v":6932,"av":2192813,"op":653.76,"vw":605.0476,"o":604.86,"c":603.38,"h":606.07,"l":603.38,"a":617.879,"s":1607544180000,"e":1607544240000}}

    if "stream" in price_dict:
        if "streams" in price_dict["data"]:
            if "streams" in price_dict["stream"]["data"]:
                if "AM.TSLA" in price_dict["stream"]:
                    if "vw" in price_dict["stream"]["data"]:
                        price = price_dict["data"]["vw"]
                        print(price)
                #else:
                  #  print("Key unable to be located within Json dict")

                        if float(price) < 629.00:
                             response = create_order("TSLA", 10, "buy", "market", "gtc")

                        if float(price) > 630.00:
                            response = create_order("TSLA", 10, "sell", "market", "gtc")

                        print(response)


def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)


def on_close(ws):
    print("closed connection")


def on_error(ws, error):
    print(error)


socket = "wss://data.alpaca.markets/stream"

websocket.enableTrace(True)
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close, on_error=on_error)
#ws.run_forever()
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

#response = create_order("BBY", 100, "buy", "market", "gtc") 
#print(response)



#def doji(ws, message):
#What we want to do here is filter through the json data, find the price, when price is goes down buy,
#when price goes up sell
#return json.loads(r.content)

#print(response)

#If money is lost, reduce the parameters for buy and sell price limits