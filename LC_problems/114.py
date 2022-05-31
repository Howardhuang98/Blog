#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   114.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/31 11:57  
------------      
"""
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        n = len(words)
        for i in range(0, n - 1):
            i_word = words[i]
            j_word = words[i + 1]
            i = 0
            j = 0
            while True:
                if j >= len(j_word):
                    return ""
                elif i >= len(i_word):
                    break
                elif i_word[i] != j_word[j]:
                    g.setdefault(i_word[i], [])
                    g[i_word[i]].append(j_word[j])
                    break
                else:
                    i += 1
                    j += 1
        print(g)

        def count_deg(g):
            res = []
            cnt = {}
            for k, v in g.items():
                cnt.setdefault(k, 0)
                for node in v:
                    cnt.setdefault(node, 0)
                    cnt[node] += 1
            for k, v in cnt.items():
                if v == 0:
                    res.append(k)
            return cnt

        indeg = count_deg(g)
        q = [u for u, d in indeg.items() if d == 0]
        for u in q:
            if u not in g.keys():
                break
            for node in g[u]:
                indeg[node] -= 1
                if indeg[node] == 0:
                    q.append(node)
        return ''.join(q) if len(q) == len(indeg) else ""


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["abc", "ab"]))
