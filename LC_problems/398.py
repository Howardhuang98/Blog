#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   398.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/25 21:58  
------------      
"""
import collections
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.index = collections.defaultdict(list)
        for i in range(len(nums)):
            self.index[nums[i]].append(i)


    def pick(self, target: int) -> int:
        return random.choice(self.index[target])

if __name__ == '__main__':
    s = Solution([1, 2, 3, 3, 3])
    print(s.pick(3))
