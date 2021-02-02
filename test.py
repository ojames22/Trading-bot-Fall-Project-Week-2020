import alpaca_trade_api as tradeapi

def welcome():

    api = tradeapi.REST(
        "PKRJJ2QQ0IU0TXNKXFCU",
        "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm",
        "https://paper-api.alpaca.markets"
    )

    account = api.get_account()

    balance_change = float(account.equity) - float(account.last_equity)
    print(f"Today\'s portfolio balance: " + account.equity)
    print(f"Today\'s portfolio balance change: ${balance_change}")


    if account.trading_blocked:
        print("Account is currently restricted from trading.")

    print("${} is available as buying power.".format(account.buying_power))

    print(account.last_equity)

def test():
    api = tradeapi.REST(
        "PKRJJ2QQ0IU0TXNKXFCU",
        "EWUK7R5ZnF9aou7AwhrRYlkqE3dAcM1JKhSP2Vqm",
        "https://paper-api.alpaca.markets"
    )
    
    account = api.get_account()
    if float(account.last_equity) > 100000:
        print("Hello world")

welcome()
test()