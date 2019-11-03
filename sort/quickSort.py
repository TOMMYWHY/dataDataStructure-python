def quick_sort(aList, first, last):
    if first >= last:
        return
    mid_value = aList[first] # 该位置的值被存下，总空出一个位置
    low = first # low 与 mid 指向同一个位置， 所以下面循环必须先用 high 来覆盖 low
    high = last
    while low < high:

        while low < high and aList[high] >= mid_value:
            high -= 1
        aList[low] = aList[high]
        while low < high and aList[low] < mid_value:
            low += 1
        aList[high] = aList[low]

        # 一下代码乱序： 原因是先执行 low 覆盖 high
        # while low < high and aList[low] < mid_value:
        #     low += 1
        # aList[high] = aList[low]
        # while low < high and aList[high] >= mid_value:
        #     high -= 1
        # aList[low] = aList[high]

    aList[low] = mid_value  # low == high

    quick_sort(aList, first, low - 1)
    quick_sort(aList, low + 1, last)


def __partition():
    pass


if __name__ == "__main__":
    ls = [9, 5, 3, 7, 8, 6, 5, 7, 0, 88, 12]
    print(ls)
    print("---------------")
    quick_sort(ls,0, len(ls)-1)
    print(ls)
