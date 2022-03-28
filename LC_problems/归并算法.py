def merge(A, p, q, r):
    """
    A数组分为两个部分，A[p,q],A[q,r]
    """
    L = [i for i in A[p:q]]
    R = [i for i in A[q:r]]
    # 额外的空间，储存L,R， 加上哨兵，以免i，j指针移到外面去了
    L.append(float("+inf"))
    R.append(float("+inf"))
    i = 0
    j = 0
    for k in range(p, r):
        # 小的进入
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r-1:
        q = int((r + p) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)
    return A


if __name__ == "__main__":
    a = [3,2,2,6,4,3,6]
    merge_sort(a,0,len(a))
    print(a)
