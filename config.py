CONFIG = {
    "api_key": "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
    "trading_pair": "BTC/USDT",
    "exchange": "Binance",
    "log_file": "logs/syntherra.log",
    "notification_email": "your-email@example.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "smtp_user": "your-email@example.com",
    "smtp_password": "your-password",
    "report_path": "reports/trade_report.json",
    "db_path": "data/syntherra.db",
    "data_path": "data/trade_data.csv",
    "strategy": {
        "type": "trend_following",
        "parameters": {
            "short_window": 50,
            "long_window": 200
        }
    },
    "risk_management": {
        "max_drawdown": 0.1,
        "stop_loss": 0.02,
        "take_profit": 0.05
    }
}
