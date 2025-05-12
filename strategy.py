import pandas as pd

class Strategy:
    def __init__(self, config):
        self.params = config["strategy"]["parameters"]

    def generate_signal(self, data):
        df = pd.DataFrame(data)
        df["short_ma"] = df["close"].rolling(window=self.params["short_window"]).mean()
        df["long_ma"] = df["close"].rolling(window=self.params["long_window"]).mean()

        if df["short_ma"].iloc[-1] > df["long_ma"].iloc[-1]:
            return "BUY"
        elif df["short_ma"].iloc[-1] < df["long_ma"].iloc[-1]:
            return "SELL"
        else:
            return "HOLD"
