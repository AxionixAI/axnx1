from config import CONFIG
from strategy import Strategy
from risk_management import RiskManager
from market_data import MarketData
from trade_executor import TradeExecutor
from logger import Logger
from notifier import Notifier
from performance import PerformanceTracker
from data_management.data_handler import DataHandler
from analytics.report_generator import ReportGenerator

def main():
    logger = Logger(CONFIG)
    notifier = Notifier(CONFIG)
    performance = PerformanceTracker(CONFIG)
    data_handler = DataHandler(CONFIG)
    report_generator = ReportGenerator(CONFIG)

    logger.log("Syntherra Bot Initialization...")

    try:
        market_data = MarketData(CONFIG)
        strategy = Strategy(CONFIG)
        risk_manager = RiskManager(CONFIG)
        executor = TradeExecutor(CONFIG)

        logger.log("Starting trading loop...")

        while True:
            data = market_data.fetch()
            data_handler.store(data)

            signal = strategy.generate_signal(data)
            logger.log(f"Generated Signal: {signal}")

            if risk_manager.evaluate(signal, data):
                result = executor.execute(signal, data)
                performance.track(result)
                data_handler.log_trade(result)
                notifier.send(f"Trade executed: {signal} on {CONFIG['trading_pair']}")
                logger.log(f"Trade successful: {result}")
            else:
                logger.log("Risk management blocked trade.")

            report = report_generator.generate(performance.get_summary())
            data_handler.store_report(report)

    except Exception as e:
        logger.log(f"Unexpected error: {str(e)}")
        notifier.send(f"Bot encountered an error: {str(e)}")
