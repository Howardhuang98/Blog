#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   780.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/9 11:57  
------------      
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            print(tx,ty)
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.reachingPoints(sx=1, sy=1, tx=2, ty=2))
    print(s.reachingPoints(sx=1, sy=1, tx=100000000, ty=1))
