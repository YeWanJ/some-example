from sys import exit


def Collatz(num, length):
    if num == 1:
        return length + 1
    if num % 2 == 0:
        length += 1
        return Collatz(int(num / 2), length)
    else:
        length += 1
        return Collatz(num * 3 + 1, length)


length = 0
max = 0
for i in range(1 ,1000000):
    flag = Collatz(i, length)
    if flag > max:
        x = i
        max = flag
print(max , x)
exit(0)
