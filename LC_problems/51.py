#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   51.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/9 22:14  
------------      
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        global cnt
        cnt = 0

        def merge_sort(nums, l, r):
            if r - l > 1:
                mid = (l + r) // 2
                merge_sort(nums, l, mid)
                merge_sort(nums, mid, r)
                merge(nums, l, mid, mid, r)

        def merge(nums, a, b, c, d):
            global cnt
            L = [i for i in nums[a:b]]
            R = [j for j in nums[c:d]]
            print(L,R)
            L.append(float("+inf"))
            R.append(float("+inf"))
            i = 0
            j = 0
            for x in range(a, d):
                if L[i] <= R[j]:
                    nums[x] = L[i]
                    i += 1
                    cnt +=j
                else:
                    nums[x] = R[j]
                    j += 1

        merge_sort(nums, 0, len(nums))
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([1,3,2,3,1]))
