def shellSort(alist):
    subListCount = len(alist) // 2
    while subListCount > 0:
        for startPosition in range(subListCount):
            gapInsertSort(alist, startPosition, subListCount)
        subListCount //= 2


def gapInsertSort(alist, start, gap):
    for index in range(start+gap, len(alist), gap):
        currentValue = alist[index]
        position = index
        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position -= gap
        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
