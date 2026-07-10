def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: length must be between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: must be alphanumeric only (no spaces, no symbols)
    if not s.isalnum():
        return False

    # Rule 3: must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 4: numbers can only appear at the end, and can't start with 0
    number_started = False
    for char in s:
        if number_started:
            if not char.isdigit():
                return False
        elif char.isdigit():
            number_started = True
            if char == "0":
                return False

    return True


if __name__ == "__main__":
    main()