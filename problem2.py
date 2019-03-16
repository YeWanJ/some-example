Fib1 = 1
Fib2 = 1
Fib = 0
Sum = 0

while Fib <= 4000000:
    Fib = Fib1 + Fib2
    Fib1 = Fib2
    Fib2 = Fib
    if (Fib % 2 == 0):
        Sum += Fib

print("the answer is %r." % Sum)
