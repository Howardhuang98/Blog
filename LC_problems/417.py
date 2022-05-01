import functools
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        memo = {}


        def dfs(location, visited):
            if location in memo.keys():
                return memo[location]
            x, y = location
            h = heights[x][y]
            pos = [False, False]
            if (x == 0 and y == n - 1) or (x == m - 1 and y == 0):
                pos =  [True, True]
            elif x == 0 or y == 0:
                pos = [True, False]
            elif x == m - 1 or y == n - 1:
                pos = [False, True]

            for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < m and 0 <= ny < n:
                    if heights[nx][ny] <= h and (nx, ny) not in visited:
                        a, b = dfs((nx, ny), visited+[(x,y)])
                        pos[0] = pos[0] or a
                        pos[1] = pos[1] or b

            memo[location] = pos
            return pos
        ans = []

        for x in range(m):
            for y in range(n):
                a, b = dfs((x, y), [])
                if a and b:
                    ans.append([x, y])


        return ans


if __name__ == '__main__':
    s = Solution()
    #print(s.pacificAtlantic([[11,3,2,4,14,6,13,18,1,4,12,2,4,1,16],[5,11,18,0,15,14,6,17,2,17,19,15,12,3,14],[10,2,5,13,11,11,13,19,11,17,14,18,14,3,11],[14,2,10,7,5,11,6,11,15,11,6,11,12,3,11],[13,1,16,15,8,2,16,10,9,9,10,14,7,15,13],[17,12,4,17,16,5,0,4,10,15,15,15,14,5,18],[9,13,18,4,14,6,7,8,5,5,6,16,13,7,2],[19,9,16,19,16,6,1,11,7,2,12,10,9,18,19],[19,5,19,10,7,18,6,10,7,12,14,8,4,11,16],[13,3,18,9,16,12,1,0,1,14,2,6,1,16,6],[14,1,12,16,7,15,9,19,14,4,16,6,11,15,7],[6,15,19,13,3,2,13,7,19,11,13,16,0,16,16],[1,5,9,7,12,9,2,18,6,12,1,8,1,10,19],[10,11,10,11,3,5,12,0,0,8,15,7,5,13,19],[8,1,17,18,3,6,8,15,0,9,8,8,12,5,18],[8,3,6,12,18,15,10,10,12,19,16,7,17,17,1],[12,13,6,4,12,18,18,9,4,9,13,11,5,3,14],[8,4,12,11,2,2,10,3,11,17,14,2,17,4,7],[8,0,14,0,13,17,11,0,16,13,15,17,4,8,3],[18,15,8,11,18,3,10,18,3,3,15,9,11,15,15]]))
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))