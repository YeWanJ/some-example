sum1 = 0
sum2 = 0

for i in range(100):
    sum1 += i
Mul = sum1 * sum1

for j in range(100):
    n = j * j
    sum2 += n

ans = Mul - sum2
print("The answer is:", ans)
