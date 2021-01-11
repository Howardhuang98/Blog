"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

"""


def searchMatrix(matrix: list, target: int) -> bool:
    left = len(matrix[0]) - 1
    up = 0
    header = matrix[up][left]
    if left == -1:
        return False
    else:
        while left >= 0 and up <= (len(matrix) - 1):
            header = matrix[up][left]
            if header == target:
                return True
            if up == (len(matrix) - 1) and left == 0:
                return False
            if header > target:
                left -= 1
            if header < target:
                up += 1


matrix = [[3,6,9,12,17,22],[5,11,11,16,22,26],[10,11,14,16,24,31],[10,15,17,17,29,31],[14,17,20,23,34,37],[19,21,22,28,37,40],[22,22,24,32,37,43]]
target = 20
print(searchMatrix(matrix, target))
