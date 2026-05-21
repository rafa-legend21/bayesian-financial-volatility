"""
Download S&P 500, Tesla, and Bitcoin historical prices, then create price-over-time plots.

Run:
    python scripts/01_download_and_plot_prices.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ASSETS = {
    "sp500": {"name": "S&P 500", "ticker": "^GSPC"},
    "tesla": {"name": "Tesla", "ticker": "TSLA"},
    "bitcoin": {"name": "Bitcoin", "ticker": "BTC-USD"},
}

START_DATE = "2018-01-01"
END_DATE = None


def get_close_series(data: pd.DataFrame) -> pd.Series:
    """Return the closing price series from a yfinance download."""
    if isinstance(data.columns, pd.MultiIndex):
        close = data["Close"].iloc[:, 0]
    else:
        close = data["Close"]
    return close.dropna()


def main() -> None:
    data_dir = Path("data")
    plots_dir = Path("plots")
    data_dir.mkdir(exist_ok=True)
    plots_dir.mkdir(exist_ok=True)

    for asset_id, info in ASSETS.items():
        print(f"Downloading {info['name']} ({info['ticker']})...")
        data = yf.download(info["ticker"], start=START_DATE, end=END_DATE, auto_adjust=False)

        if data.empty:
            raise RuntimeError(f"No data downloaded for {info['name']}.")

        close = get_close_series(data)
        output_csv = data_dir / f"{asset_id}_prices.csv"
        close.to_frame(name="Close").to_csv(output_csv)

        plt.figure(figsize=(10, 5))
        plt.plot(close.index, close.values)
        plt.title(f"{info['name']} Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        output_plot = plots_dir / f"{asset_id}_price_over_time.png"
        plt.savefig(output_plot, dpi=150)
        plt.close()

        print(f"Saved data to {output_csv}")
        print(f"Saved plot to {output_plot}")

    print("Done.")


if __name__ == "__main__":
    main()
