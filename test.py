i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print(i)

num = 600851475143
for m in range(2, num):
    if m * m <= num:
        if num % m == 0:
            large = num / m
            if Pri(large):
                print("The answer is: ", large)
