#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6068.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/14 23:00  
------------      
"""
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        right_i = 0
        l = 0
        ans = 0
        for left_i in range(len(tiles)):
            if left_i > 0:
                l -= tiles[left_i - 1][1] - tiles[left_i - 1][0] + 1
            left = tiles[left_i][0]
            right = left + carpetLen - 1

            while right_i < len(tiles) and tiles[right_i][1] < right:
                l += tiles[right_i][1] - tiles[right_i][0] + 1
                right_i += 1

            if right_i < len(tiles) and right >= tiles[right_i][0]:
                l += right - tiles[right_i][0] + 1
                right_i += 1
            ans = max(ans, l)
            print(l)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.maximumWhiteTiles(tiles=[[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], carpetLen=10)
