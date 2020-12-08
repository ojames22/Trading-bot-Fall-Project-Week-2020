#import alpaca_trade_api as tradeapi
#from alpaca_trade_api import StreamConn

#class PythonTradingBot :

def rec_doji

	if "streams" = ("streams" * 0.98) #after one minute
		"streams" = bar.close
		#create_order("TSLA", 125, "buy", "market", "gtc")

	if "streams" = ("streams" * 1.02)
		"streams" = bar.open
		#create_order("TSLA", 125, "sell", "market", "gtc")

	if bar.close >= bar.open and bar.open - bar.close > 0.01:
		print("Order recieved: () shares of (ticker)")
		self.alpaca.submit_order

#multilayered algo: https://www.youtube.com/watch?v=s8uyLscRl-Q

#bd=PythonTradingBot()
#bd.run()
rec_doji()