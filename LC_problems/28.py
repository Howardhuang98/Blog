#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   28.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/23 22:02  
------------      
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        for i, v in enumerate(haystack):
            if v == needle[0]:
                for j, n in enumerate(needle):
                    if i + j < len(haystack) and n == haystack[i + j]:
                        if j == len(needle) - 1:
                            return i
                    else:
                        break
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi","sipp"))