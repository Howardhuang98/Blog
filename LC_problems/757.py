#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   757.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/22 10:12  
------------      
"""
from typing import List
import sortedcontainers


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            current = intervals[i][0]
            for k in range(len(vals[i]), m):
                vals[i].append(current)
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < current:
                        break
                    vals[p].append(current)
                current += 1
            #print(vals)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.intersectionSizeTwo([[0, 1], [0, 3], [0, 2], [3, 4], [2, 5]]))
