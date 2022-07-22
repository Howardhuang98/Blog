#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   522.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/27 12:32  
------------      
"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def dfs(index, s, path, result):
            if index == len(s):
                if path:
                    result.append("".join(path))
                return
            dfs(index + 1, s, path, result)
            dfs(index + 1, s, path + [s[index]], result)

        res = set()
        x = set()
        for s in strs:
            temp = []
            dfs(0, s, [], temp)
            cur = set(temp)
            x |= cur & res
            res |= cur
            res -= x
        print(res)
        n = -1
        l = -1
        for series in res:
            if len(series)>l:
                l = len(series)
                n = 1
            elif len(series) == l:
                n += 1
        return l
if __name__ == '__main__':
    s = Solution()
    print(s.findLUSlength(["aaa","aaa","aa"]))
