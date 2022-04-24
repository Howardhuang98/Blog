#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2022424.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 20:14  
------------      
"""


def solu(a, b, c):

    def f(x):
        return x ** 3 + a * x ** 2 + b * x - c

    up = 1e6
    while f(up) < 0:
        up = up * 10
    low = 0
    while up - low > 1e-7:
        mid = (up + low) / 2
        if f(mid) < 0:
            low = mid
        else:
            up = mid
    return up


if __name__ == '__main__':
    print(solu(123, 333, 22222))
