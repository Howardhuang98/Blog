#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6038.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/10 10:51  
------------      
"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index = 0
        for i, e in enumerate(expression):
            if e == "+":
                plus_index = i
                break

        def cal(expression, l, r):
            exp = expression[l:r + 1]
            a = []
            b = []
            flag = True
            for n in exp:
                if n == "+":
                    flag = False
                    continue
                if flag:
                    a.append(n)
                else:
                    b.append(n)

            a = int("".join(a))
            b = int("".join(b))
            if expression[:l]:
                c = int(expression[:l])
            else:
                c = 1
            if expression[r + 1:]:
                d = int(expression[r + 1:])
            else:
                d = 1
            return c * (a + b) * d

        current = float("+inf")
        ans = None
        for i in range(plus_index):
            for j in range(plus_index + 1, len(expression)):
                y = cal(expression, i, j)
                if y < current:
                    ans = list(expression)
                    ans.insert(i, "(")
                    ans.insert(j + 2, ")")
                    current = y
        return "".join(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.minimizeResult("2120+02112"))
    print(s.minimizeResult("999+999"))
