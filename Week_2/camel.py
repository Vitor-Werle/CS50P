phrase = input("camelCase: ")
result = ""

for i in phrase:
    if i[0].isupper:
        result += i
    elif i.isupper():
        result += "_" + i
    else:
        result += i


print(result)