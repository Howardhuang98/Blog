#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   78.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/28 18:54  
------------      
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(index, path):
            if index == len(nums):
                res.append(path)
                return

            back(index + 1, path + [nums[index]])
            back(index + 1, path)

        back(0,[])
        print(res)


if __name__ == '__main__':
    s = Solution()
    s.subsets([1, 2, 3])
