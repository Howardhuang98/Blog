#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   497.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/9 15:08  
------------      
"""
import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.p = set()
        for rec in rects:
            a, b, x, y = rec
            for i in range(a, b + 1):
                for j in range(x, y + 1):
                    self.p.add((i, j))

    def pick(self) -> List[int]:
        return list(random.choice(list(self.p)))
