#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   917.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/31 22:46  
------------      
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        x = list(s)
        while l < r:
            if not ord('a')<=ord(x[l])<=ord('z') and not ord('A')<=ord(x[l])<=ord('Z'):
                l += 1
                continue

            if not ord('a')<=ord(x[r])<=ord('z') and not ord('A')<=ord(x[r])<=ord('Z'):
                r -= 1
                continue

            x[l], x[r] = x[r], x[l]
            l+=1
            r-=1

        return "".join(x)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))