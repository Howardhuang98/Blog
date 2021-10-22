def cut_rod(p,n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(0,n):
        q = max(q,p[i]+cut_rod(p,n-i-1))
    return q

if __name__ == '__main__':
    p = [1,5,8,9,10,17,17,20,24,30]
    result = cut_rod(p,9)
    print(result)