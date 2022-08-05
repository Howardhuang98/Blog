#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   304.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/31 10:29  
------------      
"""
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1 :
            return TreeNode(val=val)
        q = collections.deque()
        q.append(root)
        dep = 1
        while dep < depth - 1:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            dep += 1

        for node in q:
            temp = node.left
            node.left = TreeNode(val=val)
            node.left.left = temp
            temp = node.right
            node.right = TreeNode(val=val)
            node.right.right = temp
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.maximumGroups([10, 6, 12, 7, 3, 5]))
