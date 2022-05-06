#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   g.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/6 11:28  
------------      
"""
# n,m # n [2, 100w] [0, 100w] 数目 总时长
# a, b # 时间 价值
# 时间升序，每个任务只能完成一次
# 无法完成两个任务，输出0
from sortedcontainers import SortedList

if __name__ == "__main__":

    n, m = 4, 10
    # t, v = [3, 4, 5, 6], [1, 1, 6, 3]
    t, v = [6, 6, 6, 6], [1, 1, 1, 1]

    efficiency = [v[i] / t[i] for i in range(len(t))]
    print(efficiency)
    left = 0
    right = len(t) - 1
    ans = 0
    while left < right:
        while t[left] + t[right] > m:
            right -= 1
        print(left, right)
        p = right
        pos = [v[left] + v[right]]
        while p - 1 > left and efficiency[p - 1] > efficiency[p]:
            p -= 1
            pos.append(v[left] + v[p])
        ans = max(ans, max(pos))
    print(ans)
