#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   592.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/27 15:47  
------------      
"""
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def find(a, b):
            if a > b:
                a, b = b, a
            x = b
            while x % a or x % b:
                x += 1
            return x

        def tide(a,b):
            if a > b:
                a, b = b, a
            if a == 0:
                return b
            x = a
            while a%x or b%x:
                x -= 1
            return x


        nums = re.findall("[+,-]?[0-9]+/[0-9]+", expression)
        a = 0
        b = 0
        for i, n in enumerate(nums):
            temp_a, temp_b = n.split("/")
            temp_a = int(temp_a)
            temp_b = int(temp_b)
            if i == 0:
                a = temp_a
                b = temp_b
            else:
                common = find(b, temp_b)
                a = int(a * common / b + temp_a * common / temp_b)
                b = common

        t = tide(abs(a),abs(b))
        a = int(a/t)
        b = int(b/t)
        return "/".join([str(a),str(b)])


if __name__ == '__main__':
    s = Solution()
    print(s.fractionAddition("-1/2+1/2"))
