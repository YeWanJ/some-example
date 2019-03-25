# C（20,40）

mul1 = 1
mul2 = 1

for i in range(21, 41):
    mul1 *= i

for j in range(1, 21):
    mul2 *= j

result = int(mul1 / mul2)
print(result)
