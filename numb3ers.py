import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)

    if not match:
        return False

    for group in match.groups():
        if len(group) > 1 and group[0] == "0":
            return False
        if int(group) > 255:
            return False

    return True


if __name__ == "__main__":
    main()