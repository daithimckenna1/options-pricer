"""Pull real Apple option prices and plot the volatility smile."""
from datetime import datetime

import matplotlib.pyplot as plt
import yfinance as yf

from implied_vol import implied_vol

# --- Market data ---
ticker = yf.Ticker("AAPL")
S = ticker.history(period="1d")["Close"].iloc[-1]   # today's share price
expiry = next(e for e in ticker.options
              if (datetime.strptime(e, "%Y-%m-%d") - datetime.now()).days >= 30)                         # an expiry a few weeks out
calls = ticker.option_chain(expiry).calls           # table of call options

T = (datetime.strptime(expiry, "%Y-%m-%d") - datetime.now()).days / 365
r = 0.04                                            # rough risk-free rate

print(f"Share price: {S:.2f} | Expiry: {expiry} | T = {T:.3f} years")

# --- Implied vol for each strike ---
strikes, my_ivs, yahoo_ivs = [], [], []

for _, row in calls.iterrows():
    K = row["strike"]
    if row["bid"] <= 0 or not (0.8 * S < K < 1.2 * S):
        continue                                    # skip dead or far-away strikes

    market_price = (row["bid"] + row["ask"]) / 2                           # BLANK 1: midpoint of bid and ask
    iv = implied_vol(market_price, S, K, T, r)                                   # BLANK 2: call your solver

    strikes.append(K)
    my_ivs.append(iv)
    yahoo_ivs.append(row["impliedVolatility"])

# --- Chart ---
plt.plot(strikes, my_ivs, "o-", label="My implied vol")
plt.plot(strikes, yahoo_ivs, "x--", label="Yahoo's implied vol")
plt.axvline(S, color="grey", linestyle=":", label="Current share price")
plt.xlabel("Strike price (K)")
plt.ylabel("Implied volatility (σ)")
plt.title(f"AAPL volatility smile – expiry {expiry}")
plt.legend()
plt.savefig("volatility_smile.png")
plt.show()