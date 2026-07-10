def main():
    fraction = input("Fraction: ")
    x, y = convert(fraction)
    percentage = round(x / y * 100)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError("Numerator cannot exceed denominator")
    return x, y


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()