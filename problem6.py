sum1 = 0
sum2 = 0

for i in range(101):
    a = i * i
    sum1 += a

for j in range(101):
    sum2 += j
sum2 *= sum2

print(sum2 - sum1)
