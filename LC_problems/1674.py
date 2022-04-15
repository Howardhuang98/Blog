#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1674.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/14 16:59  
------------      
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0 for i in range(2 * limit + 1 + 1)]
        # diff[i+1] = 2...i

        for i in range(n // 2):
            a = max(nums[i],nums[n-i-1])
            b = min(nums[i],nums[n-i-1])
            diff[2] += 2
            diff[b+1] -= 1
            diff[a+b] -= 1
            diff[a + b + 1] += 1
            diff[a+limit+1] += 1
        ans = 1000000
        for i in range(3,2*limit+2):
            ans = min(sum(diff[:i]),ans)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.minMoves(nums=[1, 2, 4, 3], limit=4))
    print(s.minMoves([28,50,76,80,64,30,32,84,53,8],84))
    print(s.minMoves(nums=[1, 2, 1, 2], limit=2))
