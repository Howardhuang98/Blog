#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2024.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 17:49  
------------      
"""
from collections import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        滑动窗口
        """
        l = 0
        r = 0
        n = len(answerKey)
        ans = 0
        num_t = 0
        num_f = 0
        while r <= n :
            if num_t <= k or num_f <= k:
                ans = max(ans, r - l)
                if r<n:
                    if answerKey[r] == 'T':
                        num_t += 1
                    else:
                        num_f += 1
                r += 1
            else:
                if answerKey[l] == 'T':
                    num_t -= 1
                else:
                    num_f -= 1
                l += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxConsecutiveAnswers(answerKey="TTFF", k=2))
    print(s.maxConsecutiveAnswers("TFFT", k=1))
    print(s.maxConsecutiveAnswers("TTFTTFTT", k = 1))
