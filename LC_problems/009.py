#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   009.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/31 21:55  
------------      
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def mul(num):
            ans = 1
            for x in num:
                ans = ans * x
            return ans
        ans = 0
        l = 0
        for r in range(len(nums)):
            while mul(nums[l:r+1])>=k and l<r+1:
                l+=1
            print(r - l +1)
            ans += r - l +1
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], k=100))
