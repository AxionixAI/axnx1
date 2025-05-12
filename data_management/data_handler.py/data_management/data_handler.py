import pandas as pd

class DataHandler:
    def __init__(self, config):
        self.data_path = config.get("data_path", "data/trade_data.csv")

    def store(self, data):
        df = pd.DataFrame(data)
        df.to_csv(self.data_path, mode='a', header=False, index=False)

    def log_trade(self, trade):
        df = pd.DataFrame([trade])
        df.to_csv(self.data_path, mode='a', header=False, index=False)
