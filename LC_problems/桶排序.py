def bucket_sort(a:list):
    n = len(a)
    b = []
    for i in range(10):
        b.append([])
    for i in range(n):
        b[a[i]//10].append(a[i])
    for i in range(10):
        b[i] = sorted(b[i])
    for i in range(1,10):
        b[0] = b[0]+b[i]
    return b[0]

if __name__ == '__main__':
    a = [10,20,50,87,18,84,32]
    a = bucket_sort(a)
    print(a)
