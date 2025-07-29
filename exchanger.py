import requests
api_key = ""
base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/"

def CurrencyConverter(base_currency, target_currency, amount):
    url = f"{base_url}{base_currency.upper()}/{target_currency.upper()}"
    response = requests.get(url)

    if not response.ok:
        print("Error: Unable to fetch exchange rates")
        return 
    
    data = response.json()
    if data.get("result") != "success":
        print("Error: Unable to fetch exchange rates")
        return
    rate = data.get("conversion_rate")
    if rate is None:
        print("Error: Unable to fetch exchange rates")
        return
    converted_amount = round(amount * rate, 2)
    print(f"{amount} {base_currency} = {converted_amount} {target_currency}")
    print(f"Exchange rate: 1 {base_currency.upper()} = {rate} {target_currency.upper()}")

try:
    base_currency = input("Enter the base currency: ")
    target_currency = input("Enter the target currency: ")
    amount = float(input("Enter the amount: "))
    CurrencyConverter(base_currency, target_currency, amount)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"Error: {e}")



        