#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   meituan1.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/20 10:14  
------------      
"""


def solu(n: int, m: int, A: list, B: list):
    if m < n:
        A, B = B, A
        m, n = n, m
    ans = float("+inf")
    for i in range(m):
        cost = 0
        for j in range(max(m, i + n)):
            if j < i:
                cost += abs(B[j])
            elif i <= j < min(i + n,m):
                cost += min(abs(B[j]) + abs(A[j - i]), abs(B[j] - A[j - i]))
            elif j >= i + n:
                cost += abs(B[j])
            elif j >= m:
                cost += abs(A[j - i])

        print(i, cost)
        if cost < ans:
            ans = cost
    return ans


if __name__ == '__main__':
    # print(solu(1,1,[-9821],[7742]))
    print(solu(5, 4, [1, 2, 3, 4, 5], [5,0,0,0]))
