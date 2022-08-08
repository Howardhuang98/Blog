#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   联想8.5.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/5 19:19  
------------      
"""
import collections


def solu(n: int, s: str):
    c = collections.Counter(s)
    l_red = 0
    l_blue = 0
    r_red = c["r"]
    r_blue = c["b"]
    op = min(r_red + l_blue, l_blue + r_red)
    for i, c in enumerate(s):
        if s[i] == "r":
            r_red -= 1
            l_red += 1
        else:
            r_blue -= 1
            l_blue += 1

        op = min(op, min(r_red + l_blue, l_blue + r_red))
    return op




if __name__ == '__main__':
    print(solu(3, "rbrbrb"))
