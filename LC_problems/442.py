#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   442.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/13 21:15  
------------      
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        while i < len(nums):
            # 当前数字为n，他应该在 n-1位置
            n = nums[i]
            print(n)
            # 不在对应位置
            if n != (i + 1):
                # put n to [i+1]
                if nums[n-1] == n:
                    ans.add(n)
                    i += 1
                else:
                    nums[i], nums[n - 1] = nums[n - 1], nums[i]
            else:
                i+=1
            print(nums)
        return list(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))