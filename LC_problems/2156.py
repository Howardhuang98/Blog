#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2156.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/21 14:38  
------------      
"""


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        pk = power ** k

        def hash_function(i, p, m, pre):
            """
            hash(s[i:i+k],p,m) =

            """

            if not pre:
                res = 0
                for j, val in enumerate(s[i:i + k]):
                    res += (ord(val) - ord('a') + 1) * p ** j
                return res % m
            else:
                res = ((ord(s[i]) - ord('a') + 1) + p*pre - (ord(s[i + k]) - ord('a') + 1) * pk) % m
                return res

        succeed = n
        h = None
        for i in range(n - k, -1, -1):
            h = hash_function(i, power, modulo, h)
            if h == hashValue:
                succeed = i

        return s[succeed: succeed+k]


if __name__ == '__main__':
    s = Solution()
    print(s.subStrHash(s="leetcode", power=7, modulo=20, k=2, hashValue=0))
    print(s.subStrHash(s="fbxzaad", power=31, modulo=100, k=3, hashValue=32))
