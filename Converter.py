import requests

def convert_currency(amount, toCurrency, fromCurrency):

    url = f"https://api.exchangerate-api.com/v4/latest/{fromCurrency}"

    response = requests.get(url)
    data = response.json()

    exchange_rate = data['rates'][toCurrency]
    converted_amount = amount * exchange_rate

    return converted_amount

def cur():
    amount = float(input("Enter the Amount: "))
    fromCurrency = input("Enter Currency Name: ").upper()
    toCurrency = input("Enter Currency Name: ").upper()

    cc = convert_currency(amount, fromCurrency, toCurrency)
    print(cc)

def restartLoop(y):

    if y == "YES" or y == "Y" or "y":
        x = True

    elif y == "NO" or y == "N" or "n":
        x = False
        quit

x = True
while x == True:
    cur()
    print()
    y = input("Do You Want to Convert Any Other Currency?")
    print()
    restartLoop(y)
