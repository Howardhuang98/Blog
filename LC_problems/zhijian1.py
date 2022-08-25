#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   zhijian1.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/24 21:58  
------------      
"""
import collections
import math


def solu(n, m, matrix):
    row_mid = math.ceil(n / 2)
    col_mid = math.ceil(m / 2)
    left_up = [matrix[i][:col_mid] for i in range(row_mid)]
    left_down = [matrix[i][:col_mid] for i in range(row_mid, n)]
    right_up = [matrix[i][col_mid:] for i in range(row_mid)]
    right_down = [matrix[i][col_mid:] for i in range(row_mid, n)]
    print(left_up, left_down, right_up, right_down)


if __name__ == '__main__':
    print(solu(5, 5, [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ]))
