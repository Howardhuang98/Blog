#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2038.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/1 21:00  
------------      
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt = {'A':0,'B':0}
        l = 0
        for r,val in enumerate(colors):
            if val == colors[l]:
                if r-l>=2:
                    cnt[colors[l]] += 1
            else:
                l = r
            print(cnt)
        if cnt['A']>cnt['B']:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.winnerOfGame("AAAABBBB"))