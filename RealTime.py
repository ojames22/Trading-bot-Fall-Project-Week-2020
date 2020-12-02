#API_Key = 'PKRJJ2QQ0IU0TXNKXFCU'
#Secret_Key = 'EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm'

#https://www.youtube.com/watch?v=Mv6c_9FqNx4
import json
import websocket

API_Key = 'PKRJJ2QQ0IU0TXNKXFCU'
Secret_Key = 'EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm'

def open_stream(ws):
	print("Opened")
	auth_data = {
		"action": "auth"
		"params": API_Key
		#"data": {'key_id': API_Key,'secret_key': Secret_Key}
	} #Signals that the interface is ready to recieve data, logs into Alpaca with personal key id and secret key
	#creates variable auth_data, defienes course of action in order to log into alpaca 
	ws.send(json.dumps(auth_data)) #sends message, .dumps converts it to json stream. json - receives, stores, and transports data

	#channel_data = {
		#"action": "subscribe"
		#"params": "AM.TSLA"
	#}
	listen_message = {'action': 'listen','data':['streams: [AM.TSLA]']}} #TSLA specific (or any ticker) 'listens' to 'data' in the
	#TSLA stream

	ws.send(json.dumps(listen_message))
	#websocket creates a two way stream between the server and terminal/browser, 'dumps' variable listen_message into new enviroment
	#the code 'ws.send(json.dumps(...)' is important to pulling data and displaying data because it signals the relationship
	#between the stream and my terminal

def on_message(ws, message): #the websocket recieves a message and that message is displayed
	print('Recieved a message')
	print(message)

def on_close(ws):
	print('Closed connection')


socket = 'wss://data.alpaca.markets.stream' 

ws = websocket.WebSocketApp(socket, open_stream=open_stream, on_message=on_message)
ws.run_forever()

#open_stream()
#on_message()
#on_close()