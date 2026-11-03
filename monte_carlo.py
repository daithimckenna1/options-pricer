import numpy as np
from black_scholes import bs_call

def mc_call(S, K, T, r, sigma, n, seed=42):
    """Monte Carlo price of a European call."""
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt (T) * Z )
    payoffs = np.maximum (ST - K,0)
    return np.exp (-r*T) * np.mean(payoffs)

if __name__ == "__main__":
    print("Black-Scholes:", round(bs_call(100, 100, 1, 0.05, 0.2), 4))
    for n in [1_000, 10_000, 100_000, 1_000_000]:
        print(n, "paths:", round(mc_call(100, 100, 1, 0.05, 0.2, n), 4))