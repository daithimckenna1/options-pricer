from black_scholes import bs_call


def implied_vol(market_price, S, K, T, r):
    """Find the volatility that makes Black-Scholes match the market price."""
    low, high = 0.01, 3.0          # search range for sigma

    for _ in range(100):
        mid = (low + high) / 2     # try the middle
        price = bs_call(S, K, T, r, mid)

        if price > market_price:
            high = mid           # BLANK 1: price too high, so sigma is too high
        else:
            low = mid           # BLANK 2: price too low, so sigma is too low

    return mid


if __name__ == "__main__":
    # Test: we know sigma = 0.20 gives a call price of 10.4506
    iv = implied_vol(10.4506, 100, 100, 1, 0.05)
    print("Implied vol:", round(iv, 4))