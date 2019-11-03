def merge_sort(aList):
    n = len(aList)
    mid = n // 2 # 重点~！ " / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
    if n <= 1:
        return aList  # 返回最底层的只有单个元素的列表

    left_list = merge_sort(aList[:mid])
    right_list = merge_sort(aList[mid:])
    # merge(left_list,right_list)
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 无论 left_list 还是right_list 剩余，都可以追加进 result
    result += left_list[left_pointer:]  # [:] =》[] 当没有元素时切片，返回[].
    result += right_list[right_pointer:]

    return result


if __name__ == "__main__":
    ls = [9, 5, 3, 7, 8, 6, 5, 7, 0, 88, 12]
    print(ls)
    print("---------------")
    sorted_li = merge_sort(ls)
    print(sorted_li)
