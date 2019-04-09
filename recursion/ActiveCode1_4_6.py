from pythonds import Stack

rStack = Stack()


def toStr(n, base):
    converString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(converString[n])
        else:
            rStack.push(converString[n % base])
        n //= base
    res = ""
    while not rStack.isEmpty():
        res += str(rStack.pop())
    return res


print(toStr(7776, 2))
