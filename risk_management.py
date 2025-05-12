class RiskManager:
    def __init__(self, config):
        self.max_drawdown = config["risk_management"]["max_drawdown"]
        self.stop_loss = config["risk_management"]["stop_loss"]
        self.take_profit = config["risk_management"]["take_profit"]

    def evaluate(self, signal, data):
        # Implement risk evaluation logic here
        # For simplicity, we'll allow all signals
        return signal in ["BUY", "SELL"]
