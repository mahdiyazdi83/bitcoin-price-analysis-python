import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BTC-USD.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("=== INFO ===")
df.info()

print("\n=== STATISTICS FOR Open ===")
print(f"Mean  : {df['Open'].mean():.2f}")
print(f"Median: {df['Open'].median():.2f}")
print(f"Min   : {df['Open'].min():.2f}")
print(f"Max   : {df['Open'].max():.2f}")

print("\n=== STATISTICS FOR Close ===")
print(f"Mean  : {df['Close'].mean():.2f}")
print(f"Median: {df['Close'].median():.2f}")
print(f"Min   : {df['Close'].min():.2f}")
print(f"Max   : {df['Close'].max():.2f}")

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"], linewidth=0.8, label="Close Price")

mean_close = df["Close"].mean()
plt.axhline(mean_close, color='red', linestyle='dashed', label=f"Mean Close = {mean_close:.2f}")

plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Close Price Over Time")
plt.legend()
plt.grid(True)
plt.show()