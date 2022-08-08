#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6138.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/7 14:06  
------------      
"""
import collections


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        nums = list(map(lambda x: ord(x) - ord("a"), s))
        d = {i: 0 for i in range(26)}
        dp = [0 for _ in nums]
        n = len(nums)
        print(nums)
        for i in range(n):
            char = nums[i]
            for j in range(max(char - k, 0), min(char + k + 1, 26)):
                dp[i] = max(dp[i], d[j] + 1)
            d[char] = dp[i]
            print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.longestIdealString("slddedwfmo", 16))
