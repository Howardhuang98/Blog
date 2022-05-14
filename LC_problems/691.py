#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   691.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/14 10:57  
------------      
"""
import collections
import functools
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)

        @functools.lru_cache()
        def dp(mask: int) -> int:
            if mask == 0:
                return 0

            res = m+1
            for sticker in stickers:
                left = mask
                c = collections.Counter(sticker)
                for i, v in enumerate(target):
                    if mask >> i & 1 and c[v] >= 1:
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left)+1)
            return res

        res = dp((1 << m) - 1)
        if res>m:
            return -1
        else:
            return res

if __name__ == '__main__':
    s = Solution()
    print(s.minStickers(["with", "example", "science"], target="thehat"))
