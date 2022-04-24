#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20224245.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 21:39  
------------      
"""


if __name__ == '__main__':
    temp = input().split(" ")
    m = int(temp[0])
    temp = input().split(" ")
    ps = [float(x) for x in temp]

    cur = m
    for p in ps:
        a = cur / (1-p) - cur
        if a < 1.000001:
            print(int(cur))
            exit()
        b = int(a)
        if a - b >= 0.000001:
            cur += b
        else:
            cur += b - 1

    print(int(cur))