#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   532.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/16 11:23  
------------      
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n<2:
            return 0
        ans = 0
        l = 0
        r = 1
        while r<n and l<n:
            cur = abs(nums[r] - nums[l])
            if cur < k:
                r += 1
            elif cur > k:
                l += 1
            else:
                ans += 1
                l += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    s.findPairs([3, 1, 4, 1, 5],2)