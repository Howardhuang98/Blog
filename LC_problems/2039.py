#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2039.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 21:01  
------------      
"""
import collections
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # 当key不存在时会自动创建列表
        g = collections.defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        print(g)

        # 找最短路径
        q = collections.deque([0])
        saw = set([0])
        depth = 0
        distance = {}
        while q:
            size = len(q)
            for i in range(size):
                now = q.popleft()

                for child in g[now]:
                    if child not in saw:
                        saw.add(child)
                        q.append(child)
                distance[now] = depth
            depth += 1

        print(distance)

        # 开始枚举时间
        messages = []
        for i in g.keys():
            if i != 0:
                messages.append([i, 0, distance[i]])

        t = 0
        open = [True for i in patience]
        mq = collections.deque(messages)
        while mq:
            # 增发
            for i, p in enumerate(patience):
                if t == 0:
                    break
                if i == 0:
                    continue
                if t % p == 0 and open[i]:
                    mq.append([i, 0, distance[i]])
            print(mq)

            size = len(mq)
            for i in range(size):
                m = mq.popleft()
                m[2] -= 1
                if m[2] == 0:
                    # 换方向
                    if m[1] == 0:
                        m = [0, m[0], distance[m[0]]]
                        mq.append(m)
                        continue
                    # 关机器
                    elif m[0] == 0:
                        open[m[1]] = False
                        continue
                mq.append(m)

            t += 1

        return t+1


if __name__ == '__main__':
    s = Solution()
    print(s.networkBecomesIdle([[0, 1], [1, 2]], [0, 2, 1]))
    print(s.networkBecomesIdle([[0,1],[0,2],[1,2]], [0,10,10]))
