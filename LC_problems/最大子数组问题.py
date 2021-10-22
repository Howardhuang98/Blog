import time
import random
import matplotlib.pyplot as plt
"""
暴力遍历
"""


def min_subarray(a: list):
    l = 0
    r = 0
    m = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[j] - a[i]) > m:
                m = (a[j] - a[i])
                l = i
                r = j
            else:
                continue
    return l, r, m


"""
分治策略
"""


def find_cross_mid_min_array(a: list, low, mid, high):
    left = float('inf')
    left_index = 0
    right = -float('inf')
    right_index = 0

    # 寻找左侧最小值
    for i in range(low, mid):
        if a[i] < left:
            left = a[i]
            left_index = i
        else:
            continue
    for j in range(mid, high):
        if a[j] > right:
            right = a[j]
            right_index = j
        else:
            continue

    return left, left_index, right, right_index


def find_min_array(a: list, low, high):
    left = -float('inf')
    left_index = 0
    right = -float('inf')
    right_index = 0
    if low == high:
        return left, left_index, right, right_index
    else:
        mid = (low + high) // 2
        left1, left_index1, right1, right_index1 = find_min_array(a, low, mid)
        left2, left_index2, right2, right_index2 = find_min_array(a, mid+1, high)
        left3, left_index3, right3, right_index3 = find_cross_mid_min_array(a, low, mid, high)
        sum1 = right1 - left1
        sum2 = right2 - left2
        sum3 = right3 - left3
        if sum1>sum2 and sum1>sum3:
            return left1, left_index1, right1, right_index1
        if sum2>sum1 and sum2>sum3:
            return left2, left_index2, right2, right_index2
        else:
            return left3, left_index3, right3, right_index3


if __name__ == '__main__':
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7,8]
    b = [-1,-3,-5,-7]
    l, r, m = min_subarray(a)
    left, left_index, right, right_index = find_min_array(b, 0, 4)
    test = []
    time1 = []
    time2 = []
    for i in range(10000):
        test.append(random.randrange(0,100))
        start = time.time()
        left, left_index, right, right_index = find_min_array(test, 0, i+1)
        end = time.time()
        print("分治法：{}个数组，耗费{}秒".format(i, end - start))
        time1.append(end-start)
        start = time.time()
        l, r, m = min_subarray(test)
        end = time.time()
        print("暴力遍历法：{}个数组，耗费{}秒".format(i, end - start))
        time2.append(end - start)





