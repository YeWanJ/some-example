result = 1
for i in range(1, 1001):
    result *= 2

a = str(result)
sum = 0
for j in range(len(a)):
    sum += int(a[j])

print(sum)
