"""Generate a realistic synthetic historical stock CSV (OHLCV) for the notebook.

Replace data/stock_data.csv with real data (e.g. downloaded from Yahoo Finance / NSE)
as long as it has at least `Date` and `Close` columns.
"""
import numpy as np
import pandas as pd
from pathlib import Path

def generate(n_days: int = 1500, seed: int = 42, start_price: float = 100.0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2019-01-01", periods=n_days)
    drift, vol = 0.0004, 0.014
    shocks = rng.normal(drift, vol, n_days)
    t = np.arange(n_days)
    cycle = 0.0008 * np.sin(2 * np.pi * t / 120)
    close = start_price * np.exp(np.cumsum(shocks + cycle))
    open_ = np.r_[start_price, close[:-1]] * (1 + rng.normal(0, 0.002, n_days))
    high = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, 0.004, n_days)))
    low = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, 0.004, n_days)))
    volume = rng.integers(800_000, 5_000_000, n_days)
    return pd.DataFrame({
        "Date": dates, "Open": open_.round(2), "High": high.round(2),
        "Low": low.round(2), "Close": close.round(2), "Volume": volume,
    })

if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "data" / "stock_data.csv"
    out.parent.mkdir(exist_ok=True)
    df = generate()
    df.to_csv(out, index=False)
    print(f"Saved {len(df)} rows -> {out}")
