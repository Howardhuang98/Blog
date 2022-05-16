#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6069.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/14 23:40  
------------      
"""
import collections
import bisect


class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.cnt = 0

    def add(self, left, right) -> None:
        r = [x[1] for x in self.intervals]

        i = bisect.bisect_right(r, left)

        temp = self.intervals[:i]
        if len(self.intervals)!=0:
            if i == len(self.intervals):
                self.intervals.append([left, right])
                self.cnt += right - left + 1
            else:
                for j in range(i, len(self.intervals)):
                    if self.intervals[j][1] < right:
                        self.cnt -= self.intervals[j][1] - self.intervals[j][0] + 1
                        continue
                    elif self.intervals[j][0] <= right <= self.intervals[j][1]:
                        temp.append([left, self.intervals[j][1]])
                        self.cnt -= self.intervals[j][1] - self.intervals[j][0] + 1
                        self.cnt += self.intervals[j][1] - left + 1
                    else:
                        temp.append(self.intervals[j])
                self.intervals = temp
        else:
            self.intervals = [[left, right]]
            self.cnt = right - left + 1
        print(self.intervals)

    def count(self):
        return self.cnt


if __name__ == '__main__':
    c = CountIntervals()
    c.add(8, 43)
    c.add(13, 16)
    c.add(26,33)
    c.add(28,36)
    c.add(7, 10)
    print(c.count())
    c.add(5, 8)
    print(c.count())
