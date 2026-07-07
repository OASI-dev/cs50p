#inputting level
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except ValueError:
        continue
#inputting guess
    

import random
x = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1 or guess > level:
            continue
    except ValueError:
        continue
    if guess < x:
        print("Too low!")
        continue
    elif guess > x:
        print("Too high!")
        continue
    else:
        print("Just right!")
        break