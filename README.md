# Basic Time Series Forecast — Rolling Window Moving Average

A beginner-friendly notebook that forecasts a stock's closing price with a
**rolling-window moving average** and evaluates it with **MAE**.

## Task steps (all implemented in the notebook)
1. Load historical stock CSV data
2. Split into train and test periods (chronological, no shuffling)
3. Apply rolling-window moving average to predict
4. Evaluate forecast error (MAE) on the test set
5. Plot actual vs predicted series

## Project structure
```
stock_forecast_project/
├── data/stock_data.csv                  # historical OHLCV data (synthetic sample)
├── notebooks/time_series_forecast.ipynb # main deliverable
├── src/generate_data.py                 # regenerates the sample CSV
├── outputs/                             # saved plots / metrics
├── requirements.txt
└── README.md
```

## Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/time_series_forecast.ipynb
```

## Use your own data
Drop any CSV with `Date` and `Close` columns into `data/` and change `CSV_PATH`
in the first code cell of the notebook.

## Method notes
- **Rolling MA forecast (one-step-ahead):** prediction for day *t* = mean of the
  previous *W* actual closes. `shift(1)` ensures day *t* never sees its own value (no leakage).
- **Window size** is chosen using **train-set MAE only**, then evaluated once on the test set.
- **Baseline:** naive forecast (yesterday's close) is reported for comparison.
