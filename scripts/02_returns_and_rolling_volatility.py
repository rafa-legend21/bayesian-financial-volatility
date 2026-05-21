"""
Create log return and rolling volatility plots for S&P 500, Tesla, and Bitcoin.

Run this after:
    python scripts/01_download_and_plot_prices.py

Then run:
    python scripts/02_returns_and_rolling_volatility.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ASSETS = {
    "sp500": "S&P 500",
    "tesla": "Tesla",
    "bitcoin": "Bitcoin",
}


def compute_log_returns(prices: pd.Series) -> pd.Series:
    """Compute percentage log returns."""
    return (100 * np.log(prices / prices.shift(1))).dropna()


def main() -> None:
    data_dir = Path("data")
    plots_dir = Path("plots")
    plots_dir.mkdir(exist_ok=True)

    for asset_id, name in ASSETS.items():
        input_csv = data_dir / f"{asset_id}_prices.csv"

        if not input_csv.exists():
            raise FileNotFoundError(
                f"Missing {input_csv}. Run scripts/01_download_and_plot_prices.py first."
            )

        prices = pd.read_csv(input_csv, index_col=0, parse_dates=True)["Close"].dropna()
        returns = compute_log_returns(prices)

        returns_output = data_dir / f"{asset_id}_log_returns.csv"
        returns.to_frame(name="LogReturn").to_csv(returns_output)

        plt.figure(figsize=(10, 5))
        plt.plot(returns.index, returns.values)
        plt.axhline(0, linewidth=1)
        plt.title(f"{name} Log Returns")
        plt.xlabel("Date")
        plt.ylabel("Percentage Log Return")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(plots_dir / f"{asset_id}_log_returns.png", dpi=150)
        plt.close()

        rolling_20 = returns.rolling(window=20).std()
        rolling_60 = returns.rolling(window=60).std()

        plt.figure(figsize=(10, 5))
        plt.plot(rolling_20.index, rolling_20.values, label="20-day rolling volatility")
        plt.plot(rolling_60.index, rolling_60.values, label="60-day rolling volatility")
        plt.title(f"{name} Rolling Volatility")
        plt.xlabel("Date")
        plt.ylabel("Rolling Standard Deviation of Returns")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(plots_dir / f"{asset_id}_rolling_volatility.png", dpi=150)
        plt.close()

        print(f"Saved return and volatility plots for {name}")

    print("Done.")


if __name__ == "__main__":
    main()
