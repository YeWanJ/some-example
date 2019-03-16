from sys import exit

ans = 20
a = 0
while a == 0:
    ans += 20
    while ((ans % 19 == 0) and (ans % 18 == 0) and (ans % 17 == 0) and (ans % 16 == 0) and (ans % 15 == 0) and (ans % 14 == 0) and (ans % 13 == 0) and (ans % 12 == 0) and (ans % 11 == 0)):
        print("The answer is ", ans)
        exit(0)
