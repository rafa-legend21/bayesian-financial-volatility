import yfinance as yf
import matplotlib.pyplot as plt
from pathlib import Path

# Create plots folder if it does not exist
Path("plots").mkdir(exist_ok=True)

assets = {
    "S&P 500": "^GSPC",
    "Tesla": "TSLA",
    "Bitcoin": "BTC-USD"
}

start_date = "2018-01-01"
end_date = "2025-12-31"

for name, ticker in assets.items():
    data = yf.download(ticker, start=start_date, end=end_date)

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["Close"])
    plt.title(f"{name} Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.tight_layout()

    filename = name.lower().replace("&", "and").replace(" ", "_")
    plt.savefig(f"plots/{filename}_price_over_time.png")
    plt.close()

print("Price plots saved in the plots folder.")