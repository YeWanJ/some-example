def bubbleSort(alist):
    for passNum in range(len(alist)-1, 1, -1):
        for i in range(passNum):
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
    print(alist)


list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(list)
