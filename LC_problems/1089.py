#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1089.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/17 10:18  
------------      
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j, e in zip(range(i + 1, n), [0] + arr[i + 1:n - 1]):
                    print(j, e)
                    arr[j] = e
                i += 2
            else:
                i += 1
