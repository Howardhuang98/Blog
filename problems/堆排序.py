class Heap:
    """
    定义堆类
    """

    def __init__(self, a: list):
        self.list = a

    def parent_index(self, i):
        return (i - 1) // 2

    def left_index(self, i):
        return 2 * i + 1

    def right_index(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        """
        维持最大堆
        :param i:
        :return:
        """
        l = self.left_index(i)
        r = self.right_index(i)
        if r < len(self.list):  # 左右都有子节点
            if self.list[l] > self.list[r] and self.list[l] > self.list[i]:
                self.list[l], self.list[i] = self.list[i], self.list[l]
                self.max_heapify(l)
            if self.list[r] > self.list[l] and self.list[r] > self.list[i]:
                self.list[r], self.list[i] = self.list[i], self.list[r]
                self.max_heapify(r)
        if l < len(self.list) and r >= len(self.list):  # 只有左
            if self.list[l] > self.list[i]:
                self.list[l], self.list[i] = self.list[i], self.list[l]
        if l >= len(self.list):  # 无子节点
            pass

        return self.list

        return self.list


def build_max_heap(a):
    heapa = Heap(a)
    for i in range((len(a) - 1) // 2, -1, -1):
        heapa.max_heapify(i)
    return heapa.list


def heap_sort(a):
    r = 0
    heapa = Heap(a)
    a = build_max_heap(a)
    for i in range((len(a) - 1), 0, -1):
        heapa.list[0], heapa.list[i] = heapa.list[i], heapa.list[0]
        heapa.max_heapify(0)
    return a


if __name__ == '__main__':
    a = [16, 20, 10, 8, 7, 9, 100]
    a = build_max_heap(a)
    print(a)
    b = [16, 20, 10, 8, 7, 9, 100]
    b = heap_sort(b)
    print(b)
