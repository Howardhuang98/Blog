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


def merge(a: list, p: int, q: int, r: int):
    """
    将p-q,q-r合并，这两段是有序的
    """
    counter = 0
    i = 0
    j = 0
    L = a[p:q]
    R = a[q:r]
    L.append(int('inf'))
    R.append(int('inf'))
    for t in range(p, r):
        if L[i] > R[j]:
            a[t] = R[j]
            j += 1
            counter += len(L)
        else:
            a[t] = L[i]
            i += 1

    return counter


def find_inversion2(a: list,p,r):
    q = int(r/2)
    if p+1<r:
        find_inversion2(a,p,q)
        find_inversion2(a,q,r)
        counter = merge(a,p,q,r)
    return a


if __name__ == '__main__':
    result = find_inversion(a=[1, 5, 3, 2, 512, 3])
    result = find_inversion2(a=[1, 5, 3, 2, 512, 3],p=0,r=6)
    print(result)
