import sys

def main():
    valid_arguments()

    try:
         with open(sys.argv[1], "r") as file:
            lines = file.readlines()
         
    except FileNotFoundError:
         sys.exit("File does not exist")

    count_lines = 0
    for line in lines:
         if check_comments_and_spaces(line) == False:
              count_lines += 1
    print(count_lines)
        

def valid_arguments():
    if len(sys.argv) > 2:
          sys.exit("Too many command-lines arguments")
    if len(sys.argv) < 2:
          sys.exit("Too few command-lines arguments")
    if ".py" not in sys.argv[1]:
          sys.exit("Not a python file")

def check_comments_and_spaces(line):
     if line.isspace():
          return True
     if line.lstrip().startswith('#'):
          return True
     return False

if __name__ == "__main__":
     main()