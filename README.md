# Bayesian Financial Volatility Analysis

## Introduction

This repository provides a concise demonstration of financial time series techniques used to understand how market risk changes over time.

Instead of trying to predict stock prices directly, this demonstration focuses on volatility, uncertainty, and risk dynamics. In financial data, periods of calm and periods of stress often appear in clusters. This makes time series techniques especially useful for understanding when markets become more uncertain and how that uncertainty evolves.

## Motivation

Financial markets do not move with constant risk. Some periods are relatively stable, while others experience large and persistent fluctuations.

One important pattern in financial time series is **volatility clustering**. This means that large market movements are often followed by more large movements, while calm periods tend to remain calm.

This idea is useful in:

- financial risk monitoring
- portfolio management
- actuarial and insurance risk analysis
- derivative pricing
- stress testing
- quantitative finance

## Main Question

This demonstration focuses on the question:

> How does market risk change over time?

More specifically, it explores:

- When does the market become more volatile?
- Do periods of market stress persist?
- How can changing uncertainty be measured dynamically?
- Why are constant-variance assumptions often unrealistic in financial data?

## Data

The analysis can be applied to historical financial market data such as:

- S&P 500
- Apple
- Tesla
- Bitcoin
- exchange rates

The S&P 500 is a natural first choice because it represents broad market behavior and clearly shows volatility changes during different financial periods.

## Asset Price Overview

Before applying financial time series techniques, the first step is to visualize the raw price movement of each asset.

The three assets selected here represent different types of financial behavior:

- S&P 500: broad market index
- Tesla: individual high-growth stock
- Bitcoin: cryptocurrency with large price swings

### S&P 500 Price Over Time

![S&P 500 Price Over Time](plots/sandp500_price_over_time.png)

The S&P 500 provides a broad view of overall market movement and is useful for understanding general market trends.

### Tesla Price Over Time

![Tesla Price Over Time](plots/tesla_price_over_time.png)

Tesla is useful for observing the behavior of an individual stock with large price movements and strong volatility.

### Bitcoin Price Over Time

![Bitcoin Price Over Time](plots/bitcoin_price_over_time.png)

Bitcoin is useful for demonstrating highly volatile financial behavior and sharp changes across time.

## Methodology

### 1. Convert Prices to Log Returns

Instead of analyzing raw prices directly, financial time series models usually work with returns.

The log return is defined as:

```math
y_t = 100 * \log\left(\frac{S_t}{S_{t-1}}\right)
```

where:
- S_t is the asset price at time t 
- y_t is the percentage log return

Log returns make price movements easier to compare across time.


### 2. Visualize Return Behavior

After computing log returns, the return series is plotted over time.

Typical patterns include:

- returns fluctuating around zero
- occasional extreme movements
- periods where large movements appear close together

These patterns suggest that financial volatility is not constant.


### 3. Identify Volatility Clustering

Volatility clustering means that high-volatility periods tend to be followed by more high-volatility periods.

This is important because it shows that financial risk can persist over time instead of appearing randomly and independently.

### 4. Compute Rolling Volatility

Rolling volatility is computed using rolling standard deviation windows, such as:

- 20 trading days
- 60 trading days

This provides a simple time-varying measure of market uncertainty.

Rolling volatility often increases during:

- financial crises
- economic shocks
- geopolitical uncertainty
- major market corrections

### 5. Interpret Hidden Volatility Dynamics

In financial time series analysis, volatility can be viewed as a hidden process.

The returns are observed, but the true level of market uncertainty is not directly observed. This motivates stochastic volatility models and Bayesian approaches.

## Bayesian Perspective

Bayesian methods allow uncertainty to be modeled probabilistically.

Instead of producing only one fixed volatility estimate, Bayesian inference can provide:

- posterior distributions
- uncertainty intervals
- latent volatility estimates

This is useful because financial markets are uncertain and constantly evolving.

## Why This Matters

These techniques are useful because financial risk is not constant.

They help answer practical questions such as:

Is the market currently calm or stressed?
Are large price movements becoming more frequent?
How should short-term risk be monitored?
When might simple constant-risk models underestimate uncertainty?

Rather than focusing only on price prediction, financial time series analysis helps us understand the structure and evolution of market risk.

## Techniques Demonstrated

This repository gives a basic demonstration of several financial time series ideas:

| Technique | Purpose | Practical Use |
|---|---|---|
| Log Returns | Convert prices into comparable financial movements | Return analysis and risk modeling |
| Rolling Volatility | Measure how risk changes over time | Market risk monitoring |
| Volatility Clustering | Observe whether high-risk periods persist | Stress detection and portfolio risk |
| Hidden Volatility | Treat market uncertainty as an unobserved process | Stochastic volatility modeling |
| Bayesian Perspective | Quantify uncertainty around estimates | Probabilistic risk analysis |

## Repository Structure
bayesian-financial-volatility/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│
├── scripts/
│   ├── download_data.py
│   ├── returns_analysis.py
│   ├── rolling_volatility.py
│   └── bayesian_sv_model.py
│
├── plots/
│   ├── price_series.png
│   ├── returns_series.png
│   ├── volatility_clustering.png
│   └── rolling_volatility.png
│
└── notebooks/
    └── analysis.ipynb

## Possible Extensions

Future extensions could include:

- stochastic volatility modeling
- Bayesian MCMC estimation
- Hidden Markov Models
- regime-switching models
- particle filtering
- probabilistic forecasting

## Tools

Possible tools for implementation:

- Python
- pandas
- numpy
- matplotlib
- yfinance
- PyMC
- ArviZ

## Disclaimer

This repository is for educational and demonstration purposes only. It is not financial advice or an investment recommendation.
