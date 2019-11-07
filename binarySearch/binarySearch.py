def binary_search(a_list, item):
    n = len(a_list)
    if n > 0:
        mid = n // 2
        if a_list[mid] == item:
            return True
        elif item < a_list[mid]:
            return binary_search(a_list[:mid], item)
        else:
            return binary_search(a_list[mid + 1:], item)
    return False


def binary_search_2(a_list, item):
    n = len(a_list)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if a_list[mid] == item:
            return True
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    li = [0, 3, 5, 5, 6, 7, 7, 8, 9, 12, 88]
    print(binary_search(li, 12))
    print(binary_search_2(li, 6))
