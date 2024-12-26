import sys
import requests


def main():
    # Ensure the user provided one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    # Parse the number of Bitcoins
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number.")

    # Get the current Bitcoin price
    try:
        price = get_bitcoin_price()
    except requests.RequestException:
        sys.exit("Error: Could not fetch Bitcoin price.")

    # Calculate the cost
    total_cost = bitcoins * price

    # Output the result
    print(f"${total_cost:,.4f}")


def get_bitcoin_price():
    """
    Fetch the current Bitcoin price in USD from CoinDesk's API.
    Returns the price as a float.
    Raises requests.RequestException for network issues.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses (4xx or 5xx)

    data = response.json()  # Parse the JSON response
    return data["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()
