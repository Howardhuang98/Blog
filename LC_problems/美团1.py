#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   美团1.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/13 16:31  
------------      
"""

def solution(n: int, t: int, deadlines:list):
    deadlines.sort()
    cur = 0
    ans = 0
    for time in deadlines:
        if time >= cur+t:
            cur += t
        else:
            ans += 1
    return ans

if __name__ == '__main__':
    print(solution(6,5,[5,6,7,8,9,10]))
    print(solution(6, 5, [100, 101, 102, 103, 104, 105]))

