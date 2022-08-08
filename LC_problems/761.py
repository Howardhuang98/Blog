#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   761.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/8 11:50  
------------      
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def traval(s: str):
            print(s)
            if len(s) <= 2:
                return s

            cnt = 0
            left = 0
            ans = []
            for i in range(0,len(s)):
                char = s[i]
                if char == "1":
                    cnt += 1
                else:
                    cnt -= 1
                    if i != 0 and cnt == 0:
                        ans.append('1'+traval(s[left+1:i])+'0')
                        left = i + 1
            ans.sort(reverse=True)
            return "".join(ans)

        return traval(s)

if __name__ == '__main__':
    s = Solution()
    print(s.makeLargestSpecial("101100101100"))