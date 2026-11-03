import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from black_scholes import bs_call, bs_put, bs_delta, bs_vega

st.title("Options Pricer")
st.write("Black–Scholes pricing for a European option. Move the sliders to see the price and Greeks update.")

# --- Inputs ---
S = st.slider("Share price (S)", 50.0, 150.0, 100.0)
K = st.slider("Strike price (K)", 50.0, 150.0, 100.0)
T = st.slider("Years to expiry (T)", 0.1, 3.0, 1.0)
r = st.slider("Interest rate (r)", 0.0, 0.10, 0.05)
sigma = st.slider("Volatility (σ)", 0.05, 0.80, 0.20)

# --- Calculations ---
call = bs_call(S, K, T, r, sigma)     # call price
put = bs_put(S, K, T, r, sigma)     # put price
delta = bs_delta(S, K, T, r, sigma)     # call delta
vega = bs_vega(S, K, T, r, sigma)     # vega

# --- Results ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Call price", f"{call:.2f}")
col2.metric("Put price", f"{put:.2f}")
col3.metric("Delta", f"{delta:.3f}")
col4.metric("Vega", f"{vega:.2f}")

# --- Chart ---
S_values = np.linspace(50, 150, 200)
fig, ax = plt.subplots()
ax.plot(S_values, bs_call(S_values, K, T, r, sigma), label="Call price")
ax.plot(S_values, np.maximum(S_values - K, 0), "--", label="Payoff at expiry")
ax.axvline(S, color="grey", linestyle=":", label="Current share price")
ax.set_xlabel("Share price (S)")
ax.set_ylabel("Option value")
ax.legend()
st.pyplot(fig)