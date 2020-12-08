import ssl
import websocket, json

API_Key = "PKRJJ2QQ0IU0TXNKXFCU"
Secret_Key = "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm"

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