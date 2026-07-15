months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
        else:
            parts = date.split(" ")
            m = months.index(parts[0]) + 1
            d = int(parts[1].replace(",", ""))
            y = int(parts[2])

        if m < 1 or m > 12 or d < 1 or d > 31:
            continue

        print(f"{y:04}-{m:02}-{d:02}")
        break

    except (ValueError, IndexError):
        continue