def partition(a: list, p, r):
    """
    分割函数   分为 [p,q-1] [q] [q+1,r]
    :param a: 列表
    :param p: 第0个数
    :param r: 第r个数 包括在其中
    :return:
    """
    x = a[r]
    j = -1  # 分割指针，处于分割位置
    for i in range(0, r):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[j + 1], a[r] = a[r], a[j + 1]
    return j+1

def quick_sort(a:list,p=None,r=None):
    """
    快速排序
    :param a:
    :param p:
    :param r:
    :return:
    """
    if p == None and r == None:
        p = 0
        r = len(a)-1
    if p < r:
        q = partition(a,p,r)
        quick_sort(a,p,q-1)
        quick_sort(a,q+1,r)
    return a


if __name__ == '__main__':
    a = [1,75, 55, 12, 5, 7, 10]
    quick_sort(a)
    print(a)
