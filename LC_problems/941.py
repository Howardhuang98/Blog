#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   941.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/28 18:54  
------------      
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        Flag = True
        for i, v in enumerate(arr):
            if i == 0:
                continue
            if Flag:
                if v > arr[i - 1]:
                    continue
                else:
                    flag = False
                    continue
            if not flag:
                if v < arr[i - 1]:
                    continue
                else:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    s.validMountainArray([2,0,2])