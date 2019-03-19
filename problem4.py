from sys import exit


for M in range(999, 99, -1):
    for N in range(999, 99, -1):
        ans = M * N
        ans = str(ans)
        if ans == ans[::-1]:
            print(
                " the largest palindrome made from the product of two 3-digit numbers is: ", ans)
            exit(0)
