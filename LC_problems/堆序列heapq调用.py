import heapq

"""
python自带最大/最小堆算法，带有一系列的堆维护功能，可以直接调用
实现最大优先队列，三个主要功能
插入
最大
去掉最大
增加

"""


def insert(a):
    pass


if __name__ == '__main__':
    a = [4,2,9,18,8]
    heapq.heapify(a)  # 最大堆化
    heapq.heappop(a)
    print(a)
