#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6075.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/22 10:33  
------------      
"""
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) < 2:
            return 0
        stockPrices.sort(key=lambda x: x[0])
        k = [(p1 - p0) / (d1 - d0) for (d0, p0), (d1, p1) in zip(stockPrices[:-1], stockPrices[1:])]
        b = [y - j * x for (x, y), j in zip(stockPrices[:-1], k)]
        print([(i, j) for i, j in zip(k, b)])
        return len(set([(i, j) for i, j in zip(k, b)]))

# class Solution:
#     def minimumLines(self, stockPrices: List[List[int]]) -> int:
#         if len(stockPrices) < 2:
#             return 0
#         stockPrices.sort(key=lambda x: x[0])
#         k = [(p1 - p0) / (d1 - d0) for (d0, p0), (d1, p1) in zip(stockPrices[:-1], stockPrices[1:])]
#         ans = 1
#         print(k)
#         for i,v in enumerate(k):
#             if i == 0:
#                 continue
#             else:
#                 if not abs(v - k[i-1])<1e-10:
#                     ans += 1
#         return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]))
