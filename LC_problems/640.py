#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   640.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/10 10:46  
------------      
"""
import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        left,right = equation.split('=')
        left = '+'+left
        right = '+'+right
        lop = re.findall("[+,-][0-9]*x*",left)
        rop = re.findall("[+,-][0-9]*x*",right)
        #ax = b
        a,b = 0,0
        print(lop,rop)
        for op in lop:
            if op[-1] == 'x':
                if len(op)==2:
                    op = op[:-1]+'1x'
                a += int(op[:-1])
            else:
                b -= int(op)
        for op in rop:
            if op[-1] == 'x':
                if len(op)==2:
                    op = op[:-1]+'1x'
                a -= int(op[:-1])

            else:
                b += int(op)
        print(a,b)
        if a==0 and b == 0:
            return "Infinite solutions"
        elif a==0 and b!=0:
            return "No solution"
        else:
            return f"x={int(b/a)}"

if __name__ == '__main__':
    s = Solution()
    print(s.solveEquation("2x+3x-6x=x+2"))