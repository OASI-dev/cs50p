x = input("camelCase: ")
result = ""

for char in x:
    if char.isupper():
        result = result + "_" + char.lower()
    else:
        result = result + char

print("snake_case:", result)