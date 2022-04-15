#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2170.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/15 21:22  
------------      
"""
import collections
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even = []
        odd = []
        for i, val in enumerate(nums):
            if i % 2 == 0:
                even.append(val)
            else:
                odd.append(val)
        e = collections.Counter(even)
        e = e.most_common(2)
        while len(e)<2:
            e.append((-1, 0))
        o = collections.Counter(odd)
        o = o.most_common(2)
        while len(o)<2:
            o.append((-1, 0))
        if e[0][0] == o[0][0]:
            return len(nums) - max(e[0][1] + o[1][1], e[1][1] + o[0][1])
        else:
            return len(nums) - (e[0][1] + o[0][1])


if __name__ == '__main__':
    s = Solution()
    print(s.minimumOperations([3]))
    print(s.minimumOperations([1, 2, 2, 2, 2]))
