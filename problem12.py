from sys import exit


def getFactor(num):
    count = 1
    sum = 0
    while(count * count < num):
        if(num % count == 0):
            sum += 1
        count += 1
    sum *= 2
    if(count * count == num):
        sum += 1
    return sum


found = False
number = 1
i = 2
while(not found):
    if(getFactor(number) > 500):
        print(number)
        found = True
        exit(0)
    number += i
    i += 1
