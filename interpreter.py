x = input("Expression: ")
parts = x.split(" ")

a = float(parts[0])
operator = parts[1]
b = float(parts[2])

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)