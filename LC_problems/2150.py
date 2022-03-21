#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2150.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/21 10:29  
------------      
"""
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        all_num = set(nums)
        ans = set()
        removed = set()
        for i in nums:
            if i - 1 in all_num or i + 1 in all_num:
                continue
            else:
                if i in ans:
                    ans.remove(i)
                    removed.add(i)
                elif i in removed:
                    continue
                else:
                    ans.add(i)

        return list(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.findLonely([10, 6, 5, 8]))
    print(s.findLonely([1, 3, 5, 3]))
    print(s.findLonely([1, 4, 5, 5, 5]))
