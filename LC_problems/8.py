#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/5 17:55  
------------      
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        reading = False
        res = ""
        for char in s:
            if reading:
                if ord("0")<=ord(char)<=ord("9"):
                    res = res + char
                else:
                    break
            elif char == "+" or char =="-" or ord("0")<=ord(char)<=ord("9"):
                reading = True
                if char == "+" or char =="-":
                    if char == "-":
                        res += "-"
                    continue
                else:
                    res = res + char
                    continue
        res = int(res)
        if res >= 2**31-1:
            return 2**31-1
        elif res <= -2**31:
            return -2**31
        else:
            return res
if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("words and 987"))