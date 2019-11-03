def bubble_sort(aList):
    for i in range(0, len(aList) - 1):
        count = 0
        for j in range(0, len(aList) - i - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]
                count += 1
        if 0 == count:
            return


if __name__ == "__main__":
    ls = [9, 5, 3, 7, 8, 6, 5]
    print(ls)
    print("---------------")
    bubble_sort(ls)
    print(ls)
