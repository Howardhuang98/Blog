#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   875.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/7 12:05  
------------      
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        l = 1
        r = max(piles)
        while l < r - 1:
            print(l, r)
            mid = (l + r) // 2
            print(mid)
            m = map(lambda x: math.ceil(x / mid), piles)
            t = sum(m)
            # print(t)
            # 吃慢了
            if t > h:
                l = mid + 1
            elif t == h:
                r = mid
            # 吃快了
            elif t < h:
                r = mid
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed(
        [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316,
         877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818))
