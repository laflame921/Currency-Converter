# 💱 Currency Converter – Python CLI App

A simple command-line currency converter built with Python using the ExchangeRate-API.

---

## 🚀 Features

- Converts between any two currencies
- Uses real-time exchange rates from ExchangeRate-API
- Easy-to-use command-line interface

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install the `requests` library:

```bash
pip install requests
```

---

## 🧪 Usage

1. Replace the placeholder `api_key` in the script with your actual ExchangeRate-API key.
2. Run the script:

```bash
python converter.py
```

3. Follow the prompts:

```text
Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., NZD): NZD
Enter the amount: 100

100 USD = 165.42 NZD
Exchange rate: 1 USD = 1.6542 NZD
```

---

## 🔐 Notes

- **Keep your API key private**. Do not commit it to public repositories.
- To secure it better, consider:
  - Using a `.env` file (with `python-dotenv`)
  - Or storing the key in an environment variable

---

## 📁 Optional Project Enhancements

- Add support for `.env` files
- Build a fallback "offline mode" using hardcoded rates
- Build a simple Tkinter GUI or convert to a web app
