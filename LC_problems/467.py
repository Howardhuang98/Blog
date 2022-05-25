#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   467.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/25 16:18  
------------      
"""
import math
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        print(dp)
        return sum(dp.values())



if __name__ == '__main__':
    s = Solution()
    print(s.findSubstringInWraproundString("zabca"))
