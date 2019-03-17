from sys import exit


def Pri(N):
    for i in range(2, N):
        for j in range(2, N):
            if i * j == N:    # 证明非质数
                return False
        if i * i <= N:
            continue
        else:
            return False
    return True


num = 600851475143
for m in range(2, num):
    if m * m <= num:
        if num % m == 0:
            large = num // m
            if Pri(large):
                print("The answer is: ", large)
                exit(0)
            else:
                continue
        else:
            continue
    else:
        continue