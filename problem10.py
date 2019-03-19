import math


def IsPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 0
prime = []
for j in range(2, 2000000):
    if IsPrime(j):
        prime.append(j)
print(sum(prime))
