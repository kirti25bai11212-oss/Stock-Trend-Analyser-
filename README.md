# Stock Trend Viewer

A simple and beginner-friendly Python project to **analyze and visualize stock price trends** using built-in sample data.

## What This Project Does

This program simulates stock analysis by:

* Calculating key statistics (average, highest, lowest price)
* Measuring daily price changes
* Computing percentage changes
* Visualizing trends using graphs

It’s designed for **students and beginners** learning Python, NumPy, and data visualization.

## Features

*  Stock price trend graph
*  Moving average (3-day)
*  Daily price changes (absolute + %)
*  Summary statistics (mean, max, min)
*  No external data file needed

## Requirements

Make sure you have **Python 3** installed.

Install required libraries:
pip install numpy matplotlib

## Installation & Setup

1. **Download or clone this repository**
git clone https://github.com/your-username/stock-trend-viewer.git
```

2. **Navigate to the project folder**
cd stock-trend-viewer

##  How to Run

Run the Python script:
python stockanalyzer.py

##  How It Works

### 1. Sample Data

The program uses predefined stock prices:
prices = [100, 102, 101, 105, 110, 108, 112, 115]

You can edit these values in the code to test different scenarios.

### 2. Analysis Performed

* Average price → `np.mean()`
* Highest price → `np.max()`
* Lowest price → `np.min()`
* Daily change → `np.diff()`
* Percentage change → formula-based calculation
<img width="1680" height="2990" alt="code" src="https://github.com/user-attachments/assets/5ce72689-515c-421d-88ee-6e4d777eb141" />


### 3. Visualization

Two graphs are generated:

1. **Stock Price Trend**

   * Line chart with markers
   * Includes moving average
<img width="1245" height="829" alt="Screenshot 2026-03-26 224535" src="https://github.com/user-attachments/assets/84a8454b-4168-4f42-a94d-64d6e5672353" />



2. **Daily Changes**

   * Bar chart (price changes)
   * Line plot (percentage changes)
<img width="1249" height="712" alt="Screenshot 2026-03-26 224020" src="https://github.com/user-attachments/assets/067b5b2b-9d3e-4c56-8d7e-9ff88896cfcf" />

### Terminal Output
<img width="985" height="269" alt="Screenshot 2026-03-27 003542" src="https://github.com/user-attachments/assets/11ba6428-99f3-4022-85e7-c25138ff35eb" />


STOCK TREND VIEWER

 Stock Summary:
Average Price: 106.62
Highest Price: 115.00
Lowest Price: 100.00


### Graphs

* Trend line with moving average
* Daily fluctuations

## Customization

You can easily:

* Change stock prices
* Adjust moving average window
* Increase number of data points
* Modify graph styles

## Use Cases

* Learning Python basics
* Practicing NumPy operations
* Understanding data visualization
* Mini academic project

## Future Improvements

*  Live stock data (API integration)
*  GUI interface
*  Advanced indicators (RSI, MACD)
* File input support
