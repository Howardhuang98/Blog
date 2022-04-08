#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/8 12:02  
------------      
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        covert = {1000: "M",900: "CM", 500: "D",400: "CD", 100: "C",90: "XC", 50: "L",40: "XL", 10: "X",9: "IX", 5: "V", 4:"IV" , 1: "I"}
        ans = ""
        for n in covert:
            d, num = divmod(num, n)
            ans += covert[n] * d
        return ans


if __name__ == '__main__':
    s = Solution()
    s.intToRoman(1994)
