import numpy
"""
输入变量为
a = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
的矩阵计算
a*b = c
"""

"""
遍历法，复杂度为n^3
"""


def matrix_multiply(a, b):
    n = len(a)
    row = []
    c = []
    for i in range(0, n):
        for j in range(0, n):
            num = 0
            for k in range(0, n):
                num += a[i][k] * b[k][j]
            row.append(num)
        c.append(row)
        row = []
    return c







if __name__ == '__main__':
    a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    b = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    c = matrix_multiply(a, b)
    print(c)
