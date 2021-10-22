def binary_search(a: list, target: int):
    a = sorted(a)
    Left = 0
    right = len(a)
    index = int((Left + right) / 2)
    while a[index] != target and abs(right - Left) > 1:
        if a[index] > target:
            right = index
            index = int((index + Left) / 2)

        else:
            left = index
            index = int((index + right) / 2)

    if a[index] != target:
        print("target was not found")
    else:
        return index


def binary_search2(a, target):
    mid = int(len(a) / 2)
    if a[mid] == target:
        return mid
    if a[mid] < target:
        return binary_search2(a[mid:], target)
    if a[mid] > target:
        return binary_search2(a[:mid], target)


if __name__ == "__main__":
    index = binary_search2(a=[1, 2, 4, 234, 588, 600], target=600)
    print(index)
