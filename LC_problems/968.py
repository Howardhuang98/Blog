#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   968.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 19:58  
------------      
"""
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode):
        """
        广度优先搜索按层计算
        """
        q = deque()
        q.append(root)
        height = 0
        nums = []
        while q:
            size = len(q)
            nums.append(size)
            for i in range(size):
                current = deque.popleft()
                if current.right:
                    q.append(current.right)
                if current.left:
                    q.append(current.left)
            height += 1

        """
        nums[i] 是第i层树的节点数目
        """
        dp = [0 for _ in nums]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(nums)):
            dp[i] = min(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]