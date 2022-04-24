#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20224243.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 21:11  
------------      
"""
from typing import List


def solu(red: List, blue: List, bins: List):
    """
    红点坐标
    蓝点坐标
    区间
    """
    up = max(max(red), max(blue))
    low = min(min(red), min(blue))
    memo_red = [0 for i in range(up + 1)]
    memo_blue = [0 for i in range(up + 1)]
    for dot in red:
        memo_red[dot] += 1

    for dot in blue:
        memo_blue[dot] += 1

    ans = [0, 0, 0]
    for b in bins:
        l, r = b
        num_red = sum(memo_red[:r + 1]) - sum(memo_red[:l])
        num_blue = sum(memo_blue[:r + 1]) - sum(memo_blue[:l])
        if num_red > num_blue:
            ans[0] += 1
        elif num_red == num_blue:
            ans[1] += 1
        else:
            ans[2] += 1
    return ans


if __name__ == '__main__':
    print(solu([1, 15, 3, 10], [6, 2, 4], [[1, 2], [1, 3], [2, 6], [1, 20]]))
