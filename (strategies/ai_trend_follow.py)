import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load

class AITrendFollow:
    def __init__(self, model_path="models/trading_model.pkl"):
        self.model = load(model_path)

    def generate_signal(self, data):
        df = pd.DataFrame(data)
        df['price_change'] = df['close'].pct_change()
        df['volume_change'] = df['volume'].pct_change()
        features = df[['price_change', 'volume_change']].fillna(0).tail(1)

        prediction = self.model.predict(features)
        confidence = self.model.predict_proba(features)[0].max()

        if confidence >= 0.85:
            return "BUY" if prediction[0] == 1 else "SELL"
        return "HOLD"
