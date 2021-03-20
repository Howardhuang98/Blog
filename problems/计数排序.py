def counting_sort(a:list):
    k = max(a)
    b = []
    c = []
    for i in range(k+1):
        c.append(0)
    for j in range(len(a)):
        c[a[j]] += 1
        b.append(0)
    for i in range(1,k+1):
        c[i] = c[i]+c[i-1]
    for j in range(len(a)-1,-1,-1):
        b[c[a[j]]-1] = a[j]
        c[a[j]] -=1
    return b

if __name__ == '__main__':
    a = [1,8,7,2,4,6]
    b = counting_sort(a)
    print(b)