#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6037.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/10 10:31  
------------      
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        a = []
        b = []
        for n in str(num):
            n = int(n)
            if n % 2 == 0:
                a.append(n)
            else:
                b.append(n)
        a.sort()
        a.reverse()
        b.sort()
        b.reverse()
        i,j=0,0
        ans = [0 for n in str(num)]
        for index,n in enumerate(str(num)):
            n = int(n)
            if n % 2 == 0:
                ans[index] = a[i]
                i+=1
            else:
                ans[index] = b[j]
                j += 1
        res = 0
        ans.reverse()
        for i,val in enumerate(ans):
            res += val*(10**i)
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.largestInteger(1234))
    print(s.largestInteger(115646541615348643154896132165465165489435165465))

