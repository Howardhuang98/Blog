#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   美团2.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/13 16:04  
------------      
"""


def solution(n: int, m: int, k: int, instructs: str):
    map = set()
    x, y = 0, 0
    for i, op in enumerate(instructs):
        if op == 'W':
            x -= 1
            x = max(0, x)
        elif op == 'S':
            x += 1
            x = min(x, n - 1)
        elif op == 'A':
            y -= 1
            y = max(0, y)
        else:
            y += 1
            y = min(y, m - 1)
        map.add((x, y))
        if len(map) == n * m:
            print("Yes")
            print(i)
            return

    print("No")
    print(m * n - len(map))


if __name__ == '__main__':
    solution(2, 2, 5, "SDWAS")
