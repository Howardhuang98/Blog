#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1005.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/21 21:07  
------------      
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:

        f_n = len(first)
        s_n = len(second)
        if abs(f_n - s_n) >= 2:
            return False

        i = 0
        j = 0
        modified = False
        while i < f_n and j < s_n:
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                if modified:
                    return False
                # 可以修改
                else:
                    modified = True
                    if f_n > s_n:
                        i += 1
                    elif f_n < s_n:
                        j += 1
                    elif f_n == s_n:
                        j += 1
                        i += 1
        return True
if __name__ == '__main__':
    s = Solution()
    print(s.oneEditAway(first = "pale",second = "ple"))
    print(s.oneEditAway(first="pales", second="pal"))
    print(s.oneEditAway(first="ac", second="aa"))