#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   meituan4.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/20 11:03  
------------      
"""


def solu(n: int, A: list, B: list, C: list, distance: list):
    def man_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    a, b, c = distance
    i = distance.index(min(distance))
    r = distance[i]
    x, y = [A, B, C][i]
    ans = set()
    for temp_x in range(x, x + r + 1):
        for temp_y in range(y, y + r + 1):
            m_distance = abs(temp_x - x) + abs(temp_y - y)
            if m_distance == r:
                for possible in [[temp_x, temp_y], [2 * x - temp_x, temp_y], [temp_x, 2 * y - temp_y],
                                 [temp_x, 2 * y - temp_y]]:
                    print(possible)
                    if man_distance(possible, A) == a and man_distance(possible, B) == b and man_distance(possible,
                                                                                                          C) == c:
                        ans.add((possible[0], possible[1]))
    ans = sorted(list(ans))
    return ans[0]


if __name__ == '__main__':
    print(solu(3, [2, 1], [2, 2], [2, 3], [2, 1, 2]))
