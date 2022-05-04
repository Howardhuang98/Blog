#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   420.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/2 14:43  
------------      
"""
import re
from heapq import heappush, heappop
from itertools import groupby

def function(x,y):
    print(x+y)

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        lack = 3 - sum(bool(re.search(reg, password)) for reg in ['[a-z]', '[A-Z]', '[0-9]'])
        if n < 6:
            return max(6 - n, lack)
        pq = []
        for _, g in groupby(password):
            a = len(list(g))
            if a >= 3:
                # 使用优先队列，a%3=0的时候优先处理
                heappush(pq, (a % 3, a))
        res = 0
        print(pq)
        # 这是在过长的情况下使用策略进行删除
        while pq and n > 20:
            _, a = heappop(pq)
            if a > 3:
                # 删除1个
                heappush(pq, ((a - 1) % 3, a - 1))
            n -= 1
            res += 1
            #  去除过长的连续数组 + 删除过长  + 删除连续数组（20以内的）
        return res + max(0, n - 20) + max(sum(a // 3 for _, a in pq), lack)



if __name__ == '__main__':
    s = Solution()
    print(s.strongPasswordChecker(password="bbaaaaaaaaaaaaaaacccccc"))
