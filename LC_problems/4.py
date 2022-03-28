#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   4.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/24 19:21  
------------      
"""
if __name__ == '__main__':
    row = map(int, input().strip().split())
    n, k = [i for i in row]
    a = []
    for i in range(n):
        data = map(int, input().strip().split())
        a.append([i for i in data])
    new_a = []
    from collections import Counter

    c = Counter()
    ans = 0
    for i in range(n):
        row = tuple(a[i][j] - a[i][j - 1] for j in range(1, k))
        c += {row: 1}
    saw = []
    for k, v in c.items():
        if c[tuple([-i for i in k])]:
            if tuple([-i for i in k]) not in saw:
                ans += c[tuple([-i for i in k])] * c[k]
                saw += [k, tuple([-i for i in k])]
    print(ans)


