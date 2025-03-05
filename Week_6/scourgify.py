import csv
import sys

def main():
    # valid_arguments()

    with open("before.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in sorted(reader, reverse=True):
            print(f"{row[0]}") 

        


 
"""def valid_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    # Caso o arquivo não possa ser lido"""

if __name__ == "__main__":
    main()