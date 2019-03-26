def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        leftList = alist[:mid]
        rightlist = alist[mid:]

        mergeSort(leftList)
        mergeSort(rightlist)

        i = j = k = 0
        while i < len(leftList) and j < len(rightlist):
            if leftList[i] < rightlist[j]:
                alist[k] = leftList[i]
                i += 1
            else:
                alist[k] = rightlist[j]
                j += 1
            k += 1

        while i < len(leftList):
            alist[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightlist):
            alist[k] = rightlist[j]
            j += 1
            k += 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
