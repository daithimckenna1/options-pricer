import numpy as np
import matplotlib.pyplot as plt
from black_scholes import bs_call

K, T, r, sigma = 100, 1, 0.05, 0.2

S_values = np.linspace(50, 150, 200)        # 200 share prices from 50 to 150
prices = bs_call(S_values,K,T,r,sigma)                               # call price for every S in S_values

plt.plot(S_values, prices, label="Call price")
plt.plot(S_values, np.maximum(S_values - K,0), "--", label="Payoff at expiry")   # max(S - K, 0)
plt.xlabel("Share price (S)")
plt.ylabel("Option value")
plt.title("Black-Scholes call price vs share price")
plt.legend()
plt.show()
from black_scholes import bs_delta

deltas = bs_delta(S_values, K, T, r, sigma)                     # delta for every share price in S_values

plt.plot(S_values, deltas, label="Delta")
plt.xlabel("Share price (S)")
plt.ylabel("Delta")
plt.title("Call delta vs share price")
plt.legend()
plt.show()