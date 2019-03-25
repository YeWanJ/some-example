def bubbleSort(alist):
    exchange = True
    passNum = len(alist) - 1
    while passNum > 0 and exchange:
        exchange = False
        for i in range(passNum):
            if (alist[i] > alist[i+1]):
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passNum -= 1
    print(alist)


list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(list)
