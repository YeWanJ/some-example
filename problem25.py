a = 1 
b = 1
i = 2

while len(str(b)) < 1000:
    b , a = a + b , b 
    i += 1

print(i)