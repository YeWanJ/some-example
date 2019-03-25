def selectSort(alist):
    for passNum in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for i in range(1, passNum + 1):
            if alist[i] > alist[positionOfMax]:
                positionOfMax = i
        alist[passNum], alist[positionOfMax] = alist[positionOfMax], alist[passNum]


list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectSort(list)
print(list)
