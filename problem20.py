mul = 1
for i in range(1, 101):
    mul *= i

list = str(mul)
sum = 0
for j in range(len(list)):
    sum += int(list[j])
print(sum)
