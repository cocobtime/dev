import alpaca_trade_api as tradeapi
import time

# Replace these with your Alpaca API key and secret
API_KEY = 'PK8F6AWWC05HYF10JQJO'
API_SECRET = '8vfxI2x34kg9fBU7NavDnqtck6rk3pKIyiBnkhqr'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use the paper trading URL

# Initialize the API
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL)

def get_asset_price(symbol):
    """ Get the current price of the asset """
    barset = api.get_barset(symbol, 'minute', 1)
    bars = barset[symbol]
    return bars[0].c  # Return the closing price of the last bar

def place_order(symbol, qty, side, type, time_in_force):
    """ Place an order """
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force
        )
    except Exception as e:
        print(f"An error occurred while placing the order: {e}")

def main():
    while True:
        # Example trading logic: buy if the stock goes below a certain price
        target_stock = 'AAPL'
        current_price = get_asset_price(target_stock)
        target_price = 100  # Example target price

        if current_price < target_price:
            print(f"Buying {target_stock} at {current_price}")
            place_order(target_stock, 1, 'buy', 'market', 'gtc')

        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == '__main__':
    main()
