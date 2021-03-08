def bubble_sort(a: list):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] <= a[j + 1]:
                continue
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == '__main__':
    result = bubble_sort(a=[1, 5, 6, 3, 2, 9])
    print(result)
