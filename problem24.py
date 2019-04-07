def fact(n):
    mul = 1
    for i in range(1, n + 1):
        mul *= i
    return mul


sum1 = 1000000
astr = ''
alist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = 9
while(sum1 != 0):
    a = fact(n)
    b = alist[sum1 // a]
    astr += b
    alist.pop(sum1 // a)
    sum1 = sum1 % a
    n -= 1


for j in range(len(alist)):
    astr += alist[j]
print("The 1000001th is: ", astr)

# the number is the 1000001th, so the 1000000th is:
print("answer is : 2783915460.")
