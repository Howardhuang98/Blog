def partition(a: list, p, r):
    """
    分割函数
    对 a[p,r] 数组进行原址重排
    """
    pivot = a[r - 1]
    index = p - 1
    for i in range(p, r):
        if a[i] < pivot:
            index += 1
            a[i], a[index] = a[index], a[i]
    a[index + 1], a[r - 1] = a[r - 1], a[index + 1]
    return index + 1


def quick_sort(a: list, p=None, r=None):
    """
    快速排序
    :param a:
    :param p:
    :param r:
    :return:
    """
    if p == None and r == None:
        p = 0
        r = len(a)
    if p < r - 1:
        q = partition(a, p, r)
        quick_sort(a, p, q)
        quick_sort(a, q, r)
    return a


if __name__ == '__main__':
    a = [77, 4, 55, 12, 5, 7, 10]
    quick_sort(a)
    print(a)
