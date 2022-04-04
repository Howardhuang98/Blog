#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/3 16:18  
------------      
"""
import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        ans = [[] for j in range(numRows)]
        row = 0
        state = "down"
        for char in s:
            ans[row].append(char)
            if state == "down":
                if row == numRows-1:
                    state = "up"
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    state = "down"
                    row += 1
                else:
                    row -= 1
        result = []
        for r in ans:
            result.append("".join(r))
        return "".join(result)

if __name__ == '__main__':
    s = Solution()
    a =s.convert(s = "ABC", numRows = 1)
    print(a)
