# %%
import requests
import random
import time
import json
import os
import pandas as pd
from bs4 import BeautifulSoup

# %%
def get_stock_data():
    ticker = input("Enter the stock ticket symbol: ").strip().upper()
    url = f'https://finance.yahoo.com/quote/{ticker}'

    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 6946.55.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.'
    ]

    max_retries = 5

    for attempt in range(max_retries):
        headers = {
            'User-Agent': random.choice(user_agent_list)
        }
        
        try:
            response = requests.get(url, headers=headers)
            print(f"Status code: {response.status_code}")

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                price = soup.find('span', {'data-testid': 'qsp-price'}).text
                price_change = soup.find('span', {'data-testid': 'qsp-price-change'}).text
                price_change_percent = soup.find('span', {'data-testid': 'qsp-price-change-percent'}).text

                print(f"Stock: {ticker}")
                print(f"Price: {price}")
                print(f"Price change: {price_change}")
                print(f"Price change percent: {price_change_percent}")

                stats_labels = [label.text for label in soup.select('div[data-testid="quote-statistics"] ul li span:first-child')]
                stats_values = [value.text for value in soup.select('div[data-testid="quote-statistics"] ul li span:last-child')]

                financial_data = dict(zip(stats_labels, stats_values))

                for label, value in financial_data.items():
                    print(f"{label}: {value}")

                data = {
                    'Stock': ticker,
                    'Price': price,
                    'Price Change': price_change,
                    'Price Change Percent': price_change_percent,
                    **financial_data
                }

                with open(('stock_holder_data.json'), 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                
                df = pd.DataFrame(list(data.items()), columns=['Data', 'Value'])
                df.to_csv('stock_holder_data.csv', index=False)
                df.to_excel('stock_holder_data.xlsx', index=False)

                return data
            
            elif response.status_code == 429:
                print("Wait...")
                time.sleep(10 * (attempt+1))
            
            else:
                print(response.status_code)
                break
        
        except Exception as e:
            print(e)
    
    print("Failed to get data")
    return {}

# %%
data = get_stock_data()


