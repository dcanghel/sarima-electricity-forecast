# Modular SARIMA Electricity Forecasting

This project forecasts daily electricity demand in the PJM region using real data from the U.S. EIA API and a SARIMA model.

## Project Structure

```
electricity-sarima-modular/
├── data/           # CSV files: raw and cleaned demand
├── docs/           # Documentation, external links
├── notebooks/      # Colab or Jupyter notebooks
├── plots/          # Forecast and time series plots
├── src/            # Python modules (data, model, forecast)
│   ├── download_data.py
│   └── model_sarima.py
└── README.md
```

## Quick Start

1. Install requirements:
```bash
pip install pandas matplotlib statsmodels requests
```

2. Run `src/download_data.py` to fetch real-time demand data.

3. Use `src/model_sarima.py` to train and forecast demand.

---

✅ Modular  
📈 Real EIA API  
🧠 SARIMA for energy forecasting  
💼 Great for portfolios  
