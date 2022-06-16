#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   730.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/10 13:48  
------------      
"""


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        ans = set()
        for i in range(n):
            for j in range(i+1, n+1):
                cur = s[i:j]
                #print(cur)
                if len(cur) % 2 == 0:
                    l = len(cur) // 2

                    if cur[:l] == cur[l:][::-1]:
                        ans.add(cur)
                else:
                    l = len(cur) // 2
                    if cur[:l] == cur[l + 1:][::-1]:
                        ans.add(cur)
        print(ans)
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    s.countPalindromicSubsequences("bccb")
