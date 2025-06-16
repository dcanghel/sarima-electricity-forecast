# model_sarima.py
# Train and forecast using SARIMA model

from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarima(y, order=(1,1,1), seasonal_order=(1,1,1,7)):
    model = SARIMAX(y, order=order, seasonal_order=seasonal_order)
    results = model.fit()
    return results

def forecast_sarima(model_fit, steps=14):
    return model_fit.forecast(steps=steps)
