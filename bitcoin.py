import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    price = data["bitcoin"]["usd"]
except requests.RequestException:
    sys.exit("Error fetching data")

total = amount * price
print(f"${total:,.4f}")
#dont know why its failing