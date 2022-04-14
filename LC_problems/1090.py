#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1090.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/13 21:12  
------------      
"""
import collections
from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        memo = {}
        data = [i for i in zip(values, labels)]
        data.sort(key=lambda x: -x[0])
        data.reverse()
        res = 0
        while numWanted > 0 and data:
            val, label = data[-1][0], data[-1][1]

            if label in memo:
                if memo[label] < useLimit:
                    res += val
                    numWanted -= 1
                    memo[label] += 1
                    data.pop()
                else:
                    data.pop()
                    continue
            else:
                memo[label] = 1
                res += val
                numWanted -= 1
                data.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    #print(s.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], numWanted=3, useLimit=1))
    print(s.largestValsFromLabels(values=[9, 8, 8, 7, 6], labels=[0, 0, 0, 1, 1], numWanted=3, useLimit=2))
