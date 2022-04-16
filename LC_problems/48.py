#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   48.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/16 14:13  
------------      
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return

        for ceng in range(n//2):
            i = 1
            while i < n-2*ceng:
                i += 1
                pre = matrix[0+ceng][0+ceng]
                index = [0+ceng, 1+ceng]
                state = "r"
                while index != [ceng, ceng]:
                    x, y = index
                    matrix[x][y], pre = pre, matrix[x][y]
                    if state == "r":
                        if y == n - 1-ceng:
                            state = "d"
                        else:
                            index[1] = y + 1
                    if state == "d":
                        if x == n - 1-ceng:
                            state = "l"
                        else:
                            index[0] = x + 1
                    if state == "l":
                        if y == ceng:
                            state = "u"
                        else:
                            index[1] = y - 1
                    if state == "u":
                        index[0] = x - 1
                matrix[ceng][ceng] = pre


if __name__ == '__main__':
    s = Solution()
    s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
