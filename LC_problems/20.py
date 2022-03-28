#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/23 11:04  
------------      
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pre = set()
        opp = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in [')', '}', ']']:
                if opp[i] in pre:
                    pre.discard(opp[i])
                    continue
                else:
                    return False
            if i in ['(', '{', '[']:
                pre.add(i)
        if pre:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"))