import numpy as np
from scipy.stats import norm

def bs_call(S, K, T, r, sigma):
    """Black-Scholes price of a European call option."""
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) /(sigma * np.sqrt(T))  
    d2 =  d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T)  * norm.cdf(d2)

def bs_put(S, K, T, r, sigma):
    """European put: the right to SELL at K."""
    return bs_call(S,K,T,r,sigma) - S + K * np.exp(-r * T)
    
def bs_delta(S, K, T, r, sigma):
    """Delta of a European call: how much the price moves per €1 move in S."""
    d1 = ((np.log(S/K) + (r + 0.5 * sigma**2) * T) /(sigma * np.sqrt(T)) )      
    return norm.cdf(d1)  

def bs_vega(S, K, T, r, sigma):
    """Vega: change in call price for a 1.00 change in volatility."""
    d1 = ((np.log(S/K) + (r + 0.5 * sigma**2) * T) /(sigma * np.sqrt(T)) )              # copy your (now correct!) d1 line
    return S * norm.pdf(d1) * np.sqrt(T)   
    
if __name__ == "__main__":
    print(round(bs_call(100, 100, 1, 0.05, 0.2), 4))
    print(round(bs_put(100, 100, 1, 0.05, 0.2), 4))
    print("Delta:", round(bs_delta(100, 100, 1, 0.05, 0.2), 4))
    bump = (bs_call(100.01, 100, 1, 0.05, 0.2) - bs_call(100, 100, 1, 0.05, 0.2)) / 0.01
    print("Slope check:", round(bump, 4))
    print("Vega:", round(bs_vega(100, 100, 1, 0.05, 0.2), 4))

