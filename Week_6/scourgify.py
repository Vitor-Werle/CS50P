import csv
import sys

def main():
    valid_arguments()

    with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after)


def valid_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    # Caso o arquivo não possa ser lido

if __name__ == "__main__":
    main()