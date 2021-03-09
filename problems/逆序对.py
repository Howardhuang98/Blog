def find_inversion(a: list):
    result = []
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[i] > a[i + j + 1]:
                result.append((a[i], a[i + j + 1]))
            else:
                continue
    return result


"""
使用分治算法
"""


def merge(a: list, p: int, q: int, r: int, counter):
    """
    将p-q,q-r合并，这两段是有序的
    """
    i = 0
    j = 0
    L = a[p:q]
    R = a[q:r]
    L.append(float('inf'))
    R.append(float('inf'))
    for t in range(p, r):
        if L[i] > R[j]:
            a[t] = R[j]
            j += 1
            counter += len(L) - 1 - i
        else:
            a[t] = L[i]
            i += 1

    print(counter)
    return a, counter


def merge_sort(a: list, p, r):
    counter = 0
    result = []
    if p + 1 < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        a, counter = merge(a, p, q, r, counter)
        result.append(counter)

    return a


if __name__ == '__main__':
    a = [1, 20, 10, 4, 5, 6]
    result = merge_sort(a, p=0, r=6)
    print(result)
    result2 = find_inversion(a=[1, 20, 10, 4, 5, 6])
    print(result2)
