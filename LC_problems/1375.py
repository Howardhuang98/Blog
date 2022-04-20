#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1375.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/20 17:29  
------------      
"""
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cnt = 0
        index = 0
        for i, val in enumerate(flips):
            if i == index:
                cnt += 1
            index = max(index, val)
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.numTimesAllBlue([3, 2, 4, 1, 5]))
    print(s.numTimesAllBlue([4, 1, 2, 3]))
    print(s.numTimesAllBlue([2, 1, 2, 3]))
