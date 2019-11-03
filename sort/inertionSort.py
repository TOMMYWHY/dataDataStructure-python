# coding:utf-8
def insertion_sort(aList):
    n = len(aList)
    # for i in range(1,n):

    # for j in range(i,0,-1):
    #     if aList[i] < aList[i-1]:
    #         aList[i],aList[i-1] = aList[i-1],aList[i]
    #         i-=1
    #     else:
    #         break

    # j = i
    # while i > 0:
    #     if aList[i] < aList[i-1]:
    #         aList[i],aList[i-1] = aList[i-1],aList[i]
    #         i-=1
    #     else:
    #         break

    # for i in range(1, n):
    #     cur = aList[i]
    #     j = i
    #     while j-1 >= 0 and aList[j - 1] > cur:
    #         aList[j] = aList[j - 1]
    #         j -= 1
    #     aList[j] = cur

    for i in range(1, n):
        cur = aList[i]  # 外层 i 对应的值记录下来
        prev_index = i - 1  # 当 -- 时，不会影响外层 i
        while prev_index >= 0 and aList[prev_index] > cur:
            aList[prev_index + 1] = aList[prev_index]
            prev_index -= 1
        aList[prev_index + 1] = cur


if __name__ == "__main__":
    ls = [9, 5, 3, 7, 8, 6, 5, 7, 0, 88, 12]
    print(ls)
    print("---------------")
    insertion_sort(ls)
    print(ls)
# [9, 5, 3, 7, 8, 6, 5, 7, 0, 88, 12]
# ---------------
# [0, 3, 5, 5, 6, 7, 7, 8, 9, 12, 88]
