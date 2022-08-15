#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   美团3.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/13 16:59  
------------      
"""
from collections import deque

def solution(n:int,nums:list):
    q = deque([-1 for _ in range(n)])
    for n in nums:
        for _ in range(2):
            cur = q.popleft()
            while cur != -1:
                q.append(cur)
                cur = q.popleft()
            q.append(cur)
        cur = q.popleft()
        while cur != -1:
            q.append(cur)
            cur = q.popleft()
        q.append(n)
    cur = q.popleft()
    q.append(cur)
    return list(q)

if __name__ == '__main__':
    print(solution(4,[1,2,3,4]))
