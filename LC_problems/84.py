#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   84.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 19:30  
------------      
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        全排列，是回溯法
        """
        n = len(nums)
        result = []
        existed = set()

        def backtracing(nums, path, num_path):
            if len(path) == n:
                result.append([nums[i] for i in path])

            for i in range(n):
                if i not in path and num_path+str(nums[i]) not in existed:
                    backtracing(nums, path + [i], num_path+str(nums[i]))
                    existed.add(num_path+str(nums[i]))

        backtracing(nums, [], "")
        print(result)


if __name__ == '__main__':
    s = Solution()
    s.permuteUnique([1,1,3])
