import ccxt

class MarketData:
    def __init__(self, config):
        exchange_class = getattr(ccxt, config["exchange"].lower())
        self.exchange = exchange_class({
            "apiKey": config["api_key"],
            "secret": config["api_secret"]
        })
        self.pair = config["trading_pair"]

    def fetch(self):
        ohlcv = self.exchange.fetch_ohlcv(self.pair, timeframe='1h', limit=200)
        data = [{"timestamp": x[0], "open": x[1], "high": x[2], "low": x[3], "close": x[4], "volume": x[5]} for x in ohlcv]
        return data
