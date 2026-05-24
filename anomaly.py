# anomaly.py
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, column='value'):
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(df[[column]])
    df['is_anomaly'] = df['anomaly'] == -1
    return df