#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1021.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/28 18:27  
------------      
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left = 0
        start = 0
        res = []
        for i, char in enumerate(s):
            if i == 0:
                if char == '(':
                    left = 1
                    start = 0
                    continue
                else:
                    return s

            if char == '(':
                left += 1

            if char == ')':
                left -= 1
                if left == 0:
                    res.append(s[start + 1:i])
                    start = i + 1

        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("(a)(a)"))
