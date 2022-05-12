#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   240.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/12 21:23  
------------      
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if m==0 or n==0:
            return False
        print(matrix[0][0],matrix[m - 1][n - 1])
        if m <= 2 and n <= 2:
            for row in matrix:
                for e in row:
                    if e == target:
                        return True
            return False
        if not matrix[0][0] <= target <= matrix[m - 1][n - 1]:
            return False

        x, y = m // 2, n // 2
        lu = [row[0:y + 1] for row in matrix[0:x + 1]]
        ld = [row[0:y + 1] for row in matrix[x + 1:]]
        ru = [row[y + 1:] for row in matrix[0:x + 1]]
        rd = [row[y + 1:] for row in matrix[x + 1:]]
        if matrix[x][y] >= target:
            return self.searchMatrix(lu, target) or self.searchMatrix(ru, target) or self.searchMatrix(ld, target)
        else:
            return self.searchMatrix(ld, target) or self.searchMatrix(ru, target) or self.searchMatrix(rd, target)


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[4,5],
                          [4,6],
                          [9,14],
                          [10,15]],7))
