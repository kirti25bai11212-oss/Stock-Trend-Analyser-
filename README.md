# Stock Trend Viewer

A simple and beginner-friendly Python project to analyze and visualize stock price trends using built-in sample data.

## What This Project Does

This program simulates stock analysis by:

* Calculating key statistics (average, highest, lowest price)
* Measuring daily price changes
* Computing percentage changes
* Visualizing trends using graphs

It is designed for students and beginners learning Python, NumPy, and data visualization.

## Features

* Stock price trend graph
* Moving average (3-day)
* Daily price changes (absolute and percentage)
* Summary statistics (mean, max, min)
* No external data file required

## Requirements

Make sure you have Python 3 installed.

Install required libraries:

```bash
pip install numpy matplotlib
```


## Installation and Setup

1. Clone this repository:

```bash
git clone https://github.com/your-username/stock-trend-viewer.git
```

2. Navigate to the project folder:

```bash
cd stock-trend-viewer
```

## How to Run

Run the Python script:

```bash
python stockanalyzer.py
```

## How It Works

### 1. Sample Data

The program uses predefined stock prices:

```python
prices = [100, 102, 101, 105, 110, 108, 112, 115]
```

You can modify these values in the code to test different scenarios.

### 2. Analysis Performed

* Average price → `np.mean()`
* Highest price → `np.max()`
* Lowest price → `np.min()`
* Daily change → `np.diff()`
* Percentage change → formula-based calculation

### 3.Visualization
   <img width="1680" height="2990" alt="code" src="https://github.com/user-attachments/assets/bf7c4aec-aaa0-4f1b-876f-72f3347efd70" />

#### Stock Price Trend

* Line chart with markers
* Includes moving average
  
<img width="1245" height="829" alt="Screenshot 2026-03-26 224535" src="https://github.com/user-attachments/assets/24ff0655-9b68-44ab-92d5-9a0ea1a32384" />


#### Daily Changes

* Bar chart for price changes
* Line plot for percentage changes

<img width="1249" height="712" alt="Screenshot 2026-03-26 224020" src="https://github.com/user-attachments/assets/7882c74b-3472-4f67-920b-a8aabfdc68b1" />

# ###Terminal Output

```
STOCK TREND VIEWER

Stock Summary:
Average Price: 106.62
Highest Price: 115.00
Lowest Price: 100.00
```
<img width="1112" height="368" alt="Screenshot 2026-03-26 224610" src="https://github.com/user-attachments/assets/2ccea45e-cc94-45ab-bdb2-ac72b2156164" />

## Graphs

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

* Live stock data using APIs
* Graphical user interface (GUI)
* Advanced indicators such as RSI and MACD
* File input support


