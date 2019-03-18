import math


def IsPrime(n):
    i = 3
    range = int(math.sqrt(n)) + 1
    while(i < range):
        if(n % i == 0):
            return False
        i += 1
    return True


i, num = 1, 3
while i < 10001:
    if IsPrime(num):
        i += 1
    num += 2
print(num - 2)
