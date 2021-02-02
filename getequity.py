import alpaca_trade_api as tradeapi

def get_account_info():

	if __name__ == "__main__":

	    api = tradeapi.REST(
	        "PKRJJ2QQ0IU0TXNKXFCU",
	        "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm",
	        "https://paper-api.alpaca.markets"
	    )

	    account = api.get_account()

	    balance_change = float(account.equity) - float(account.last_equity)
	    print(f"Today\'s portfolio balance: " + account.equity)
	    print(f"Today\'s portfolio balance change: ${balance_change}")
	    

def b_power():
	api = tradeapi.REST(
	    "PKRJJ2QQ0IU0TXNKXFCU",
	    "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm",
	    "https://paper-api.alpaca.markets"
	)

	account = api.get_account()

	if account.trading_blocked:
	    print('Account is currently restricted from trading.')

	print('${} is available as buying power.'.format(account.buying_power))


b_power()
get_account_info()