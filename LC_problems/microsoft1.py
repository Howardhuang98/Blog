#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   microsoft1.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/19 19:34  
------------      
"""


def solu(x: list, y: list, w: int) -> int:
    x.sort()
    ans = 0
    cur = 0
    while cur < len(x):
        # print(cur)
        l = cur
        r = len(x)-1
        mid = (l + r) // 2
        while l != r:
            if x[mid] > x[cur] + w:
                r = mid
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2
        cur = l
        ans += 1
    return ans


if __name__ == '__main__':
    print(solu([0, 1, 2, 3,4,5,6], [], 3))
