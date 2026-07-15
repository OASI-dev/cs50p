def main():
    time = input("What time is it? ").strip()
    t = convert(time)
    
    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <= 13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")

def convert(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours + minutes / 60

main()