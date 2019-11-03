def selection_sort(aList):
    for i in range(0, len(aList) - 1):
        min_index: int = i
        for j in range(i + 1, len(aList)):
            if aList[min_index] > aList[j]:
                min_index = j
        aList[min_index], aList[i] = aList[i], aList[min_index]


if __name__ == "__main__":
    ls = [9, 5, 3, 7, 8, 6, 5, 7, 0, 88, 12]
    print(ls)
    print("---------------")
    selection_sort(ls)
    print(ls)
