#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   282.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 15:11  
------------      
"""


class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        ans = []

        def backtrack(expr, i: int, res: int, mul: int):
            # 终止条件
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)

            # 处理节点
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+';
                    backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-';
                    backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*';
                    backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.addOperators()
