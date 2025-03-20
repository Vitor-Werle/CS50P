phrase = input("camelCase: ")
result = ""

for i in phrase:
    if i.isupper():
        result += "_" + i.lower()
    else:
        result += i


print(result)