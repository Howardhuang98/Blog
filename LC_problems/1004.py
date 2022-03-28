#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1004.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/24 19:39  
------------      
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        c = Counter([i for i in s])
        n = 0
        for k, v in c.items():
            if v % 2 != 0:
                n += 1
        if n > 1:
            return False
        else:
            return True
if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("avb"))