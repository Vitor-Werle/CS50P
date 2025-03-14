import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    pattern = r"http://www\.youtube\.com/embed/.*?\""

    match = re.search(pattern, s)


...


if __name__ == "__main__":
    main()