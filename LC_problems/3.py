#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   3.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 14:55  
------------      
"""


class Solution:
    def addOperators(self, num, target: int):


        def possible_value(num):
            """
            return all possible values in list
            """
            if len(num) == 2:
                a = int(num[0])
                b = int(num[1])
                return [a + b, a - b, a * b]
            else:
                res = []
                for i in possible_value(num[1:]):
                    res.append(int(num[0]) + i)
                    res.append(int(num[0]) - i)
                    res.append(int(num[0]) * i)
            return res

        if target in possible_value(num):
            return True


if __name__ == '__main__':
    s = Solution()
    s.addOperators([1,2],2)