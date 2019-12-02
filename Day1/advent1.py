import math, string, sys


def findFuel(x):
    x = math.floor(x / 3)
    x = x - 2

    if x > 0:
        return x + findFuel(x)
    else:
        return 0




def multi_input():
    try:
        while True:
            data=input()
            if not data: break
            yield int(data)
    except KeyboardInterrupt:
        return

userInput = list(multi_input())

total = 0
for y in userInput:
    fuel = findFuel(y)
    print(fuel)
    total= total + fuel





print("total = " + str(total))