import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start = to_24_hour(start_hour, start_minute, start_period)
    end = to_24_hour(end_hour, end_minute, end_period)

    return f"{start} to {end}"


def to_24_hour(hour, minute, period):
    hour = int(hour)
    minute = minute if minute else "00"

    if hour < 1 or hour > 12:
        raise ValueError("Hour out of range")

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()