import requests
import sys

def main():
    try:
        n = sys.argv[1]
        float(n)
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        coin(n)

def coin(value):
    data = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = data["bpi"]["USD"]["rate_float"]
    usd = float(value)
    amount = usd * rate
    print(f"${amount:,.4f}")
main()
