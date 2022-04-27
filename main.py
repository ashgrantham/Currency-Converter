from requests import get
import pprint
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
BASE_URL = "https://free.currconv.com/"
API_KEY = "4d1c6a3a6cb7e6347193"

printer = pprint.PrettyPrinter()

def get_currencies():
  endpoint = f"api/v7/currencies?apiKey={API_KEY}"
  url = BASE_URL + endpoint
  data = get(url).json()['results']
  data = list(data.items())
  data.sort()
  return data

def print_currencies(currencies):
  for name, currency in currencies:
    name = currency['currencyName']
    _id = currency['id']
    symbol = currency.get("currencySymbol", "")
    print(f"{_id} - {name} - {symbol}")
def exchange_rate(currency1, currency2):
  endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
  url = BASE_URL + endpoint
  response = get(url)
  data = response.json()
  if len(data) == 0:
    print('Invalid currencies.')
    return
  rate = list(data.values())[0]
  print(f"{currency1} -> {currency2} = {rate}")
  return rate

#data = get_currencies()
#print_currencies(data)


def convert(currency1, currency2, amount):
  rate = exchange_rate(currency1, currency2)
  if rate is None:
    return
  try:
    amount = float(amount)
  except:
    print("invalid amount.")
    return
  converted_amount = rate * amount
  print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
  return


def main():
  print(Fore.YELLOW + Style.BRIGHT+"Welcome to the currency converter!")
  print(Fore.GREEN + Style.BRIGHT+"List - lists the different currencies")
  print(Fore.BLUE + Style.BRIGHT+"Convert - convert from one currency to another")
  print(Fore.MAGENTA + Style.BRIGHT+"Rate - get the exchange rate of two currencys")
  print()
main()
while True:
  
  command = input("Enter your command" + Fore.RED + "(q to quit): " + Fore.WHITE + Style.BRIGHT + Fore.BLUE).lower()
  if command == "q":
    break
  elif command == "list":
    print_currencies(get_currencies())
  elif command == "convert":
    currency1 = input(Fore.CYAN + "Enter a base currency: ").upper()
    amount = input(Fore.YELLOW+Style.BRIGHT+"enter an amount in {}: ".format(currency1))
    currency2 = input(Fore.GREEN + Style.BRIGHT+"Enter a currency to convert to: ").upper()
    convert(currency1, currency2, amount)
  elif command == "rate":
    currency1 = input(Fore.MAGENTA + "Enter a base currency: ").upper()
    currency2 = input(Fore.YELLOW + "Enter a currency to convert to: ").upper()
    exchange_rate(currency1, currency2)
  else:
    print("unrecognized command")

    
