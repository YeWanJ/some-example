from sys import exit
import math


def IsPrime(n):
    if n % 2 == 0:
        return False
    i = 3
    for a in range(2, int(math.sqrt(n)) + 1):
        if n % a == 0:
            return False
    return True


num = 600851475143
sqrt = int(math.sqrt(num))
for large in range(sqrt + 1, 2, -1):
    if num % large == 0:
        if IsPrime(large):
            print("The largest prime factor of the number is: ", large)
            exit(0)
