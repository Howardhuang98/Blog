#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0105.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/13 11:11  
------------      
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            first, second = second, first
        diff = len(first) - len(second)
        if diff == 1:
            i, j = 0, 0
            ans = 0
            while i < len(first) and j < len(second):
                if first[i] == second[j]:
                    i += 1
                    j += 1
                elif ans < 1:
                    i += 1
                else:
                    return False
            return True

        elif diff == 0:
            if first==second:
                return True
            else:
                return False

        else:
            return False
