#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6127.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/24 13:37  
------------      
"""
import collections
from typing import List


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))

        def count(x: int):
            return collections.Counter(bin(x))["1"]

        nums = list(map(count, nums))
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        print(nums)
        while not i > j:
            print(i,j)
            if nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] >= k:
                ans += 2*(j-i)+1
                j -= 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countExcellentPairs([1,2,4,8,16,32,64,128,256],2))
