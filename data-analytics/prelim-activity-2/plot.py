import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv')

# Plot for Google stock
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Stock Price Google'], label='Google', marker='o')
plt.title('Google Stock Price Change (2015)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Price', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot for Microsoft stock
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Stock Price Microsoft'], label='Microsoft', marker='o')
plt.title('Microsoft Stock Price Change (2015)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Price', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
