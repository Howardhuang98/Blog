#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   008.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/1 12:12  
------------      
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 100001
        l = 0
        for r,val in enumerate(nums):
            while sum(nums[l:r+1]) >= target:
                ans = min(r-l+1, ans)
                l += 1
        if ans == 100001:
            return 0
        else:
            return ans



if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12]))