for c in range(500):
    for a in range(500):
        if (c * c == a * a + (1000 - a - c) * (1000 - a - c)):
            if a <= 1000 - a - c:
                print(a*(1000 - a - c)*c)
