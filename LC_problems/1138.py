#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1138.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/7 13:05  
------------      
"""
import collections


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        def pos(char: str):
            x, y = divmod(ord(char) - ord("a"), 5)
            return x, y

        current = [0, 0]
        ans = []
        for char in target:
            x, y = pos(char)
            d_x = x - current[0]
            d_y = y - current[1]
            if char != "z":
                if d_x < 0:
                    ans += ["U"] * (-d_x)
                else:
                    ans += ["D"] * d_x
                if d_y < 0:
                    ans += ["L"] * (-d_y)
                else:
                    ans += ["R"] * d_y
            else:
                if d_y < 0:
                    ans += ["L"] * (-d_y)
                else:
                    ans += ["R"] * d_y
                if d_x < 0:
                    ans += ["U"] * (-d_x)
                else:
                    ans += ["D"] * d_x
            ans.append("!")
            current = [x, y]
        return "".join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.alphabetBoardPath("code"))
