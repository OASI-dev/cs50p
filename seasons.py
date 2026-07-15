import sys
from datetime import date
from dateutil.relativedelta import relativedelta
import inflect


def main():
    birthdate = input("Date of Birth: ")

    try:
        year, month, day = birthdate.split("-")
        birth = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    difference = relativedelta(today, birth)

    total_minutes = (
        difference.years * 365 * 24 * 60
        + difference.months * 30 * 24 * 60
        + difference.days * 24 * 60
        + difference.hours * 60
        + difference.minutes
    )

    p = inflect.engine()
    words = p.number_to_words(total_minutes, andword="")

    print(f"{words.capitalize()} minutes")


if __name__ == "__main__":
    main()