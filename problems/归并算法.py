def merge(a:list,p:int,q:int,r:int):
    """
    merge函数，用于将a，分割为p-q，q-r两段
    """
    L = []
    R = []
    for i in a[p:q]:
        L.append(i)
    for i in a[q:r]:
        R.append(i)
    L.append(100000)
    R.append(100000)
    L_index = 0
    R_index = 0
    for k in range(p,r):
        if L[L_index]<R[R_index]:
            a[k] = L[L_index]
            L_index+=1
        else:
            a [k] = R[R_index]
            R_index+=1
    return a

def merge_sort(a,p,r):
    """并归排序"""
    if p+1<r:
        q = int((p+r)/2)
        merge_sort(a,p,q)
        merge_sort(a,q,r)
        merge(a,p,q,r)
    
    return a

if __name__ == "__main__":
    a = [1,3,5,7,2,5,8,10]
    a = merge(a,0,4,8)
    print(a)
    b = [1,2,4324,232,433,123,424,7]
    b = merge_sort(b,0,8)
    print(b)
