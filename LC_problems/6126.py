#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6126.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/24 12:58  
------------      
"""
import collections
from typing import List
import sortedcontainers


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cui = {}
        self.foo = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.cui.setdefault(c, sortedcontainers.SortedDict())
            self.cui[c][(r, f)] = f
            self.foo[f] = (r, c)

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, c = self.foo[food]
        self.foo[food] = (newRating, c)
        self.cui[c].pop((oldRating, food))
        self.cui[c][(newRating, food)] = food

    def highestRated(self, cuisine: str) -> str:
        return self.cui[cuisine][0]
