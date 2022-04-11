#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6039.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/10 11:20  
------------      
"""
from typing import List

from queue import PriorityQueue


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue(len(nums))
        for i in nums:
            pq.put(i)
        for i in range(k):
            n = pq.get()
            n += 1
            pq.put(n)
        ans = 1
        while not pq.empty():
            n = pq.get()
            ans = int(ans * n % (1e9+7))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([24, 5, 64, 53, 26, 38], 54))
    print(s.maximumProduct([92, 36, 15, 84, 57, 60, 72, 86, 70, 43, 16], 62))
