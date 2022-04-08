#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0051.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/8 21:28  
------------      
"""
from functools import reduce
from itertools import product
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        print(masks)
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0),
                   default=0)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(["a", "aa", "aaa", "aaaa"]))
    print(s.maxProduct(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]))
