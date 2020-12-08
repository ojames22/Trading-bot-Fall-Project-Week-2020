import requests
#import config
#from config import *

API_Key = 'PKRJJ2QQ0IU0TXNKXFCU'
Secret_Key = 'EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm'

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_Key, 'APCA-API-SECRET-KEY': Secret_Key}
#variable are defined

def get_account():
	r = requests.get(ACCOUNT_URL, headers=HEADERS)

	return json.loads(r.content)
	#finds account and returns content. Since data is better stored in a dictionary
	#of sorts, json helps store this data and make it easily visible


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


response = create_order("BBY", 18, "buy", "market", "gtc") #within the alpaca
#API there are many options for order styped to define. For example, "gtc"
#means good unti cancelled, meaning the order will be processed until it is
#completed or cancelled. Another option is "day", the order will be processed
#and cancelled if not by the end of the day. This line of code tells the function
#create_order which ticker to buy, how many shares to buy, what type of transaction,
#where to buy it, and when it should be cancelled.

print(response)