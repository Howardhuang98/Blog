#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   713.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/5 11:31  
------------      
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left=0
        prob = 1
        ans = 0
        for i,n in enumerate(nums):
            prob = prob*n
            while prob>=k:

                prob = prob/nums[left]
                left += 1
            ans += i+1-left
            print(ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.numSubarrayProductLessThanK([10,5,2,6],100)