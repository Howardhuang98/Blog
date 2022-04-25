#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   868.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 22:30  
------------      
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        print(s)
        stack = ['b']
        ans = 0
        for x in s:
            print(stack)
            if x == '1' and stack[-1] == '0':
                i = 1
                while stack[-1] == '0':
                    stack.pop()
                    i += 1
                ans = max(ans, i)
            elif x == '1' and stack[-1] == '1':
                ans = max(ans, 1)
            else:
                stack.append(x)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(6))
