import heapq

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
        for i in a[q:r]:
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

    def partition(self,p,r):
        """
        分割 [p,r+1]
        :param p:
        :param r:
        :return:
        """
        x = self.list[r]
        j = p-1  # 分割指针，处于分割位置
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
        return a

    def heap_sort(self):
        size = len(self.list)
        heapq.heapify(self.list)
        c = []
        for i in range(0,size):
            c.append(heapq.heappop(self.list))
        self.list = c
        return self.list








if __name__ == '__main__':
    a = [1, 6, 7, 3, 4, 24, 3,88,9]
    s = Sort(a)
    result = s.insert_sort()
    result2 = s.merge_sort()
    result3 = s.quick_sort()
    result4 = s.heap_sort()
    print(result4)
