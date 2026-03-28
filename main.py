import numpy as np
import matplotlib.pyplot as plt

# Sample stock data (no file needed)

def load_data():
    # Example stock prices
    prices = [100, 102, 101, 105, 110, 108, 112, 115]
    return np.array(prices)

# Analysis functions

def analyze(prices):
    avg_price = np.mean(prices)
    max_price = np.max(prices)
    min_price = np.min(prices)

    changes = np.diff(prices)
    pct_changes = (changes / prices[:-1]) * 100

    return avg_price, max_price, min_price, changes, pct_changes

# Visualization functions

def plot_prices(prices, window=3):
    plt.figure(figsize=(10,6))
    plt.plot(prices, marker='o', label="Stock Price", color='blue')

    if len(prices) >= window:
        moving_avg = np.convolve(prices, np.ones(window)/window, mode='valid')
        plt.plot(range(window-1, len(prices)), moving_avg,
                 label=f"{window}-Day Moving Avg", color='red', linestyle='--')

    plt.title("Stock Price Trend")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()

def plot_changes(changes, pct_changes):
    plt.figure(figsize=(10,5))
    plt.bar(range(len(changes)), changes, color='green', alpha=0.6, label='Daily Change')
    plt.plot(pct_changes, marker='o', color='orange', label='Percentage Change')
    plt.title("Daily Stock Changes")
    plt.xlabel("Day")
    plt.ylabel("Price Change / % Change")
    plt.legend()
    plt.grid()

# Main program

def main():
    print(" STOCK TREND VIEWER ")

    prices = load_data()

    avg, max_p, min_p, changes, pct_changes = analyze(prices)

    print("\n Stock Summary:")
    print(f"Average Price: {avg:.2f}")
    print(f"Highest Price: {max_p:.2f}")
    print(f"Lowest Price: {min_p:.2f}")

    plot_prices(prices)
    plot_changes(changes, pct_changes)

    plt.show()
    print("\n END OF ANALYSIS")

if __name__ == "__main__":
    main()
