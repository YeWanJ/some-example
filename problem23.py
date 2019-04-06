from math import sqrt


def isAbundant(n):
    sum1 = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            sum1 += (i + n/i)
        if n / i == i:
            sum1 -= i
        if sum1 > 2*n:
            return True
    return False


sum1 = sum(range(28124))
sum2 = 0
set1 = set()
for i in range(1, 28124):
    if isAbundant(i):
        set1.add(i)
    for j in set1:
        if (i - j) in set1:
            sum2 += i
            break

sum = sum1 - sum2
print(sum)
