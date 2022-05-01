import copy
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        left_trees = set(trees)
        left_trees.remove(trees[leftMost])
        p = leftMost
        while True:
            now = left_trees.pop()
            temp = []
            for r in left_trees:
                # // 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], now, r) < 0:
                    temp.append(now)
                    now = r
            left_trees = left_trees.union(temp)
            ans.append(now)

        return ans



if __name__ == '__main__':
    s = Solution()
    s.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
