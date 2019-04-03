import math


def sumDiv(num):
    sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    return sum


alist = [0 for k in range(1, 10001)]
sum = 0
for j in range(1, 10000):
    sumdiv = sumDiv(j)
    if sumdiv > j and sumdiv < 10000:
        alist[sumdiv] = j
    elif alist[j] == sumdiv:
        sum += sumdiv + j
print(sum)
