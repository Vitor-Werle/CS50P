import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    IPv4 = re.search(r"^[0-255]\.[0-255]\.[0-255]\.[0-255]$", ip)
    if IPv4:
        return True
    return False





if __name__ == "__main__":
    main()