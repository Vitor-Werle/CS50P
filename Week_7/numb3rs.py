import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    pattern = r"^((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$"

    match = re.search(pattern, ip)
    
    if match:
        return True
    return False




if __name__ == "__main__":
    main()