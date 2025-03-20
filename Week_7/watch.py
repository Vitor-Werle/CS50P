import re


def main():
    print(parse(input("HTML: ")))

# Eu não preciso limitar onde o padrão acaba pois quando não atende mais ao padrão o re.search para
def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]+)", s)
        if url_pattern:
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()