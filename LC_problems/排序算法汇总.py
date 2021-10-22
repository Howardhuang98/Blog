import heapq
import time
import random
import pandas as pd


class Sort():
    def __init__(self, a: list):
        self.list = a
        self.len = len(a)

    def insert_sort(self):
        """
        插入排序
        :return:
        """
        for i in range(1, self.len):
            j = i - 1
            key = self.list[i]
            while j >= 0 and self.list[j] > key:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key
        return self.list

    def merge(self, p: int, q: int, r: int):
        """
        merge函数，用于将a，分割为p-q，q-r两段
        """
        L = []
        R = []
        for i in self.list[p:q]:
            L.append(i)
        for i in self.list[q:r]:
            R.append(i)
        L.append(10000000)
        R.append(10000000)
        L_index = 0
        R_index = 0
        for k in range(p, r):
            if L[L_index] < R[R_index]:
                self.list[k] = L[L_index]
                L_index += 1
            else:
                self.list[k] = R[R_index]
                R_index += 1
        return self.list

    def merge_sort(self, p=None, r=None):
        """
        归并排序
        :param p:
        :param r:
        :return:
        """
        if p is None and r is None:
            p = 0
            r = len(self.list)
        """并归排序"""
        if p + 1 < r:
            q = int((p + r) / 2)
            self.merge_sort(p, q)
            self.merge_sort(q, r)
            self.merge(p, q, r)

        return self.list

    def partition(self, p, r):
        """
        分割 [p,r+1]
        :param p:
        :param r:
        :return:
        """
        x = self.list[r]
        j = p - 1  # 分割指针，处于分割位置
        for i in range(p, r):
            if self.list[i] <= x:
                j += 1
                self.list[i], self.list[j] = self.list[j], self.list[i]
        self.list[j + 1], self.list[r] = self.list[r], self.list[j + 1]
        return j + 1

    def quick_sort(self, p=None, r=None):
        """
        快速排序
        :param p: 起始
        :param r: 终止位置，默认为全部
        :return:
        """
        if p is None and r is None:
            p = 0
            r = len(self.list) - 1
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q - 1)
            self.quick_sort(q + 1, r)
        return self.list

    def heap_sort(self):
        size = len(self.list)
        heapq.heapify(self.list)
        c = []
        for i in range(0, size):
            c.append(heapq.heappop(self.list))
        self.list = c
        return self.list

    def counting_sort(self):
        k = 20000
        b = []
        c = []
        for i in range(k + 1):
            c.append(0)
        for j in range(len(self.list)):
            c[self.list[j]] += 1
            b.append(0)
        for i in range(1, k + 1):
            c[i] = c[i] + c[i - 1]
        for j in range(len(self.list) - 1, -1, -1):
            b[c[self.list[j]] - 1] = self.list[j]
            c[self.list[j]] -= 1
        self.list = b
        return self.list


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == '__main__':
    data = {}
    #data['time_of_insert'] = []
    data['time_of_merge'] = []
    data['time_of_quick'] = []
    data['time_of_heap'] = []
    data['time_of_counting'] = []
    for i in range(10, 100000, 1000):  # 做10,20,30 ...长度的实验
        test_list = random_int_list(0, 1000, i)
        """
        a = Sort(test_list)
        start = time.time()
        a.insert_sort()
        end = time.time()
        data['time_of_insert'].append(end - start)
        """
        #####
        test_list = random_int_list(0, 1000, i)
        b = Sort(test_list)
        start = time.time()
        b.merge_sort()
        end = time.time()
        data['time_of_merge'].append(end - start)
        #####
        test_list = random_int_list(0, 1000, i)
        c = Sort(test_list)
        start = time.time()
        c.quick_sort()
        end = time.time()
        data['time_of_quick'].append(end - start)
        #####
        test_list = random_int_list(0, 1000, i)
        d = Sort(test_list)
        start = time.time()
        d.heap_sort()
        end = time.time()
        data['time_of_heap'].append(end - start)
        #####
        test_list = random_int_list(0, 1000, i)
        e = Sort(test_list)
        start = time.time()
        e.counting_sort()
        end = time.time()
        data['time_of_counting'].append(end - start)
    df = pd.DataFrame(data=data)
    df.to_csv("data.csv")
