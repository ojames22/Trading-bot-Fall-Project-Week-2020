#API_Key = 'PKRJJ2QQ0IU0TXNKXFCU'
#Secret_Key = 'EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm'

#https://www.youtube.com/watch?v=Mv6c_9FqNx4

import config
import websocket

def open_stream(ws):
	print('Opened')
	auth_data = {
		'action': 'authenticate'
		'data': {'key_id': config.API_Key,'secret_key': config.Secret_Key}
	} #Signals that the interface is ready to recieve data, logs into Alpaca with personal key id and secret key

	ws.send(json.dumps(auth_data)) #sends message, .dumps converts it to json stream. json - receives, stores, and transports data

	listen_message = {'action': 'listen','data':['streams: [AM.TSLA]']}}

	ws.send(json.dumps(listen_message))


def on_message(ws, message):
	print('Recieved a message')
	print(message)

def on_close(ws):
	print('Closed connection')


socket = 'wss://data.alpaca.markets.stream'

ws = websocket.WebSocketApp(socket, open_stream=open_stream, on_message=on_message)
ws.run_forever() = 

#open_stream()
#on_message()
#on_close()