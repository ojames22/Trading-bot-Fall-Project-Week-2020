import requests
from bs4 import BeautifulSoup

def enter_ticker():
	ticker = input('Retrieve prices from ticker: ')

	val = str(ticker)
	print('Inputs are string values. Input: '+ ticker)

	URL = 'https://app.alpaca.markets/paper/stocks/' + ticker
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find('div', class_='_61e231f4')

def retrieve_price(results):
	ticker_price = results.find_all('div',class_='_fdd6a588')

	current_price = ticker.find('div', class_='_c7985158').get_text()

	print(current_price)

enter_ticker()
retrieve_price()