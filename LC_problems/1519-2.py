#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1519-2.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 18:10  
------------      
"""
import collections


class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        g = collections.defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(o: int, pre: int):
            """"
            进入子节点，并且

            """
            print("进入",o)
            f[o][ord(labels[o]) - ord("a")] = 1
            for nex in g[o]:
                if nex != pre:
                    dfs(nex, o)

                    for i in range(26):
                        f[o][i] += f[nex][i]
            print("出", o)
            #print(o,f)

        f = [[0] * 26 for _ in range(n)]
        dfs(0, -1)

        ans = [f[i][ord(labels[i]) - ord("a")] for i in range(n)]
        return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.countSubTrees(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd")
    print(ans)