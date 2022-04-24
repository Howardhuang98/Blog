#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6043.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 11:00  
------------      
"""

from collections import defaultdict
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        end = max(flowers,key=lambda x:x[1])
        start = min(flowers,key=lambda x:x[0])
        num_flowers = [0 for i in range]




if __name__ == "__main__":
    s = Solution()
    print(s.countRectangles([[1, 2], [2, 3], [2, 5]], [[2, 1], [1, 4]]))
    # print(s.countRectangles([[1, 1], [2, 2], [3, 3]], [[1, 3], [1, 1]]))
    # print(s.countRectangles([[1, 1], [2, 2], [3, 3], [3, 2], [4, 2]], [[1, 1]]))
