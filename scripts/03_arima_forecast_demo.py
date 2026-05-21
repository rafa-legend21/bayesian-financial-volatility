"""
Basic ARIMA forecasting demonstration.

This script uses the S&P 500 as the first forecasting example.
The goal is to demonstrate the workflow, not to claim perfect financial prediction.

Run this after:
    python scripts/01_download_and_plot_prices.py

Then run:
    python scripts/03_arima_forecast_demo.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

ASSET_ID = "sp500"
ASSET_NAME = "S&P 500"
FORECAST_STEPS = 60


def main() -> None:
    data_dir = Path("data")
    plots_dir = Path("plots")
    plots_dir.mkdir(exist_ok=True)

    input_csv = data_dir / f"{ASSET_ID}_prices.csv"

    if not input_csv.exists():
        raise FileNotFoundError(
            f"Missing {input_csv}. Run scripts/01_download_and_plot_prices.py first."
        )

    prices = pd.read_csv(input_csv, index_col=0, parse_dates=True)["Close"].dropna()

    if len(prices) <= FORECAST_STEPS + 100:
        raise ValueError("Not enough data for the forecasting demonstration.")

    train = prices.iloc[:-FORECAST_STEPS]
    test = prices.iloc[-FORECAST_STEPS:]

    model = ARIMA(train, order=(1, 1, 1))
    fitted_model = model.fit()

    forecast = fitted_model.forecast(steps=FORECAST_STEPS)
    forecast.index = test.index

    plt.figure(figsize=(10, 5))
    plt.plot(train.index[-300:], train.iloc[-300:], label="Training data")
    plt.plot(test.index, test.values, label="Actual test data")
    plt.plot(forecast.index, forecast.values, label="ARIMA forecast")
    plt.title(f"{ASSET_NAME} ARIMA Forecast Demonstration")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(plots_dir / f"{ASSET_ID}_arima_forecast.png", dpi=150)
    plt.close()

    comparison = pd.DataFrame({
        "Actual": test,
        "Forecast": forecast,
    })
    comparison.to_csv(data_dir / f"{ASSET_ID}_arima_forecast_comparison.csv")

    print(f"Saved ARIMA forecast plot to plots/{ASSET_ID}_arima_forecast.png")
    print(f"Saved forecast comparison to data/{ASSET_ID}_arima_forecast_comparison.csv")
    print("Done.")


if __name__ == "__main__":
    main()
