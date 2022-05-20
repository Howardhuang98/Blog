#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   436.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/20 13:43  
------------      
"""
import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        temp = [(i, l, r) for i, (l, r) in enumerate(intervals)]
        temp.sort(key=lambda x: x[1])
        l_list = [x[1] for x in temp]
        ans = [-1 for _ in temp]
        for i, l, r in temp:
            right = r
            index = bisect.bisect_left(l_list, right)
            if index == len(temp):
                ans[i] = -1
            else:
                ans[i] = temp[index][0]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findRightInterval([[1,4],[2,3],[3,4]]))
    print(s.findRightInterval([[3,4],[2,3],[1,2]]))
