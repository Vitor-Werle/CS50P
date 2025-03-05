from tabulate import tabulate
import csv
import sys

def main():
    valid_argument()

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            print(tabulate(reader, tablefmt="grid"))
    except FileNotFoundError:
         sys.exit("File does not exist")

def valid_argument():
    if len(sys.argv) > 2:
          sys.exit("Too many command-lines arguments")
    if len(sys.argv) < 2:
          sys.exit("Too few command-lines arguments")
    if ".csv" not in sys.argv[1]:
          sys.exit("Not a python file")


if __name__ == "__main__":
    main()