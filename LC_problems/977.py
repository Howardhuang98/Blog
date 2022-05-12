#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   977.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/11 21:15  
------------      
"""
from itertools import pairwise
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))  # 空间复杂度为 O(m)，改用下标枚举可以达到 O(1)




if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["zyx","wvu","tsr"]))
