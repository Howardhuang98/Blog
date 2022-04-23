#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   396.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/22 10:42  
------------      
"""
from functools import reduce
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        current = sum(map(lambda x: x[0] * x[1], zip(nums, range(len(nums)))))
        ans = current
        for i in range(1, len(nums)):
            n = nums[len(nums) - i]
            current -= n * (len(nums) - 1)
            current += sum(nums[:len(nums) - i])
            current += sum(nums[len(nums) - i + 1:])
            ans = max(ans, current)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxRotateFunction([4, 3, 2, 6]))
    print(s.maxRotateFunction([100]))
