# Yahoo-Finance-Scraper

## Overview

Yahoo Finance Scraper is a Python tool designed to retrieve and process financial data from Yahoo Finance. This project consists of scripts that extract real-time stock prices, financial metrics, and historical data, storing them in structured formats for analysis. Additionally, utilities for transposing stock data files are included.

## Features

- Fetches stock prices, price changes, and percentage changes from Yahoo Finance
- Extracts key financial metrics such as market cap, PE ratio, EPS, volume, and 52-week range
- Supports multiple output formats, including CSV, Excel, and JSON
- Includes tools to transpose financial data for better readability and analysis
- Implements randomized user-agents and retry mechanisms to handle web requests efficiently

## Components

### `scraper.py`
- Fetches financial data for a user-specified stock ticker.
- Retrieves real-time stock prices, percentage changes, and financial statistics.
- Saves the data in JSON, CSV, and Excel formats.

### `transpose.py`
- Reads an Excel file containing stock data.
- Transposes the data to improve readability.
- Saves the transposed data as a new Excel file.

### `transpose_many.py`
- Processes multiple Excel stock data files at once.
- Transposes each file and merges them into a combined dataset.
- Outputs the final result as an Excel file.

**Note:** Each of these scripts also has a corresponding Jupyter Notebook (`.ipynb`) version for interactive execution.

## Installation

To use this scraper, ensure Python is installed on your system. Additionally, install the required dependencies:

1. Install Python dependencies using a package manager.
2. Ensure Excel files are available for transposing operations.
3. Run the appropriate script or Jupyter Notebook as needed.

## Usage

1. **Fetching Stock Data**  
   - Run `scraper.py` to retrieve stock data.
   - Enter the stock ticker and output file names when prompted.
   - The script will fetch stock prices, financial metrics, and save the data.

2. **Transposing Data**  
   - Use `transpose.py` for a single stock data file.
   - Use `transpose_many.py` to process multiple files and merge results.

## Dependencies

This project requires the following Python libraries:
- `requests` (for fetching Yahoo Finance data)
- `beautifulsoup4` (for web scraping)
- `pandas` (for data manipulation)
