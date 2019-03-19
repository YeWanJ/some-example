
largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        strProduct = str(product)
        if strProduct == strProduct[::-1] and product > largest:
            largest = product
print(largest)
