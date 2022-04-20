#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   388.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/20 11:42  
------------      
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        stack = []
        for line in input.split('\n'):
            depth = line.count('\t')
            if depth >= len(stack):
                stack.append(len(line) - depth)
            else:
                while len(stack) > depth:
                    stack.pop()
                stack.append(len(line) - depth)
            if line.count('.'):
                # 每层都要添加depth个 /
                res = max(res, sum(stack) + depth)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
