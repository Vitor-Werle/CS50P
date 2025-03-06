import csv
import sys

def main():
    valid_arguments()

    after = []

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row["name"].split(",")
                after.append({"first": split_name[1], "last": split_name[0].rstrip(), "house": row["house"]})          

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
        
    
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in after:
            writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})

        


 
def valid_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
   

if __name__ == "__main__":
    main()