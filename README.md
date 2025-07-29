# Currency Converter – Python CLI App

A simple command-line currency converter built with Python using the ExchangeRate-API.

## Features

- Converts between any two currencies
- Uses real-time exchange rates from ExchangeRate-API
- Easy to use command-line interface

## Requirements

- Python 3.x
- `requests` library

Install the `requests` library if you don't have it:

```bash
pip install requests
Usage
Replace the placeholder api_key in the script with your actual ExchangeRate-API key.

Run the script:

bash
Copy
Edit
python converter.py
Follow the prompts to enter the base currency, target currency, and amount.

Example
mathematica
Copy
Edit
Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., NZD): NZD
Enter the amount: 100

100 USD = 165.42 NZD
Exchange rate: 1 USD = 1.6542 NZD
Notes
The API key should be kept private. Do not commit your actual key to public repositories.

You can add .env support or use environment variables for better security.

