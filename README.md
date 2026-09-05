# Meme Coin FOMO Simulator

A browser-based crypto trading practice game for learning charts, volatility, liquidity, position sizing, slippage, and meme-coin risk without using real money.

## Features

- Dark trading-terminal interface inspired by professional market dashboards
- Responsive layout for phones, tablets, laptops, and desktop screens
- Simulated practice wallet with a configurable bankroll
- Distinct meme-coin market scenarios
- Stochastic market behavior with trend, chop, panic, mean reversion, and random shocks
- OHLC candlestick chart with close-price line graph
- Tap or click anywhere on the chart to simulate a market entry
- Simulated trade feed and wallet P&L
- Rug-pull and liquidity-risk practice scenarios
- Beginner crypto learning lab
- Real OHLC CSV import for replaying verified historical data
- No wallet connection and no real funds

## Run Locally

### Option 1: Open the page directly

Open `index.html` in a modern browser.

### Option 2: Use the Python server

Python 3.10 or newer is recommended.

```bash
python server.py
```

Open this address in your browser:

```text
http://127.0.0.1:8000
```

The server also provides a health endpoint:

```text
http://127.0.0.1:8000/api/health
```

## How to Use the Simulator

1. Choose a market case.
2. Set a virtual practice bankroll.
3. Choose a position size.
4. Click **Start Trade**.
5. Watch the candles, close line, market cap, liquidity, and bonding-curve progress.
6. Tap or click the chart to simulate entering at that point in the market.
7. Use the trade controls to complete the scenario.
8. Review the simulated P&L.
9. Reset the round and compare your decision with another scenario.

## Market Scenarios

The built-in scenarios are fictionalized practice replays inspired by common public meme-coin patterns. They are not exact historical records.

- Rocket Dog: long-run community-driven moonshot
- Shelter Dog: viral narrative and supply pressure
- Green Frog: explosive attention followed by a fade
- Solana Dog: volatile two-sided chop
- Hat Dog: fast breakout with uncertain continuation
- Melon: anonymous rug-pull risk

Each round includes randomized behavior so the same scenario does not always follow the same path.

## Import Real OHLC Data

The page can import a CSV containing verified historical candle data. The file must include `open`, `high`, `low`, and `close` columns. A timestamp column is optional.

Example:

```csv
timestamp,open,high,low,close
2024-01-01,0.0000010,0.0000012,0.0000009,0.0000011
2024-01-02,0.0000011,0.0000015,0.0000010,0.0000014
2024-01-03,0.0000014,0.0000016,0.0000012,0.0000013
```

Imported data is labeled as source data in the interface. The application does not download or verify market data automatically.

## Learning Topics

The learning lab introduces:

- Expected value and probability
- Log returns and volatility
- Momentum and acceleration
- Liquidity and market impact
- Bayesian updating
- Regime changes and reflexivity
- Position sizing and drawdown control
- Why market predictions are uncertain

These concepts are educational explanations, not trading signals or financial advice.

## GitHub Pages

The static browser version can be hosted with GitHub Pages:

1. Create a public GitHub repository.
2. Upload `index.html` and `README.md`.
3. Open the repository's **Settings**.
4. Select **Pages**.
5. Choose **Deploy from a branch**.
6. Select the `main` branch and the root folder.
7. Click **Save**.

GitHub will provide a public address similar to:

```text
https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/
```

GitHub Pages runs the browser game but does not run `server.py`. Use the Python server locally or deploy it separately to a Python-capable service.

## Technology

- HTML
- CSS
- JavaScript
- SVG chart rendering
- Python standard-library HTTP server

No external packages are required.

## Important Disclaimer

This is a fictional, educational simulator. It does not connect to cryptocurrency exchanges, wallets, blockchains, or real funds. It does not provide financial advice or guarantee prediction accuracy. Real cryptocurrency markets involve substantial risk, including total loss.
