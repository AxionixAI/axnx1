import pandas as pd
from datetime import datetime

class PerformanceReport:
    def __init__(self, log_file="logs/axionix.log"):
        self.log_file = log_file

    def generate(self):
        trades = pd.read_csv(self.log_file, names=['timestamp', 'pair', 'signal', 'price', 'profit'])
        total_trades = len(trades)
        win_rate = len(trades[trades['profit'] > 0]) / total_trades * 100
        avg_profit = trades['profit'].mean()
        max_drawdown = trades['profit'].min()

        report = {
            "Total Trades": total_trades,
            "Winning Rate": f"{win_rate:.2f}%",
            "Average Profit per Trade": f"${avg_profit:.2f}",
            "Max Drawdown": f"${max_drawdown:.2f}",
            "Generated on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        print("Performance Report:")
        for key, value in report.items():
            print(f"{key}: {value}")

        return report

if __name__ == "__main__":
    reporter = PerformanceReport()
    reporter.generate()
