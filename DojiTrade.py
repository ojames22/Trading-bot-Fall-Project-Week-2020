import ssl
import websocket, json
import requests

API_Key = "PKRJJ2QQ0IU0TXNKXFCU"
Secret_Key = "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm"

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": API_Key, "secret_key": Secret_Key}
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "listen", "data": {"streams": ["AM.BBY"]}} #BBY: Best Buy Co., Inc.

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

def on_error(ws, error):
    print(error)

socket = "wss://data.alpaca.markets/stream"

websocket.enableTrace(True)
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close, on_error=on_error)
#ws.run_forever()
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})



def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    #create_order defines which type of order the API will conduct in response 
    #to the parameters defined by Alpaca and called within the function

    return json.loads(r.content)

#response = create_order("BBY", 100, "buy", "market", "gtc") 
#print(response)



def doji():
#What we want to do here is filter through the json data, find the price, when price is goes down buy,
#when price goes up sell
    for in json.dumps:
        price = {
            "stream": "data": "TSLA": "op"
        }

    if float(price) >= 103:
        response = create_order("BBY", 10, "sell", "market", "gtc")

    if float(price) <= 103:
        response = create_order("BBY", 10, "buy", "market", "gtc")

return json.loads(r.content)

print(response)

#If money is lost, reduce the parameters for buy and sell price limits