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
        if l <= len(self.list) and self.list[l] > self.list[i]:
            largest = l
        else:
            largest = i
        if r <= len(self.list) and self.list[r] > self.list[largest]:
            largest = r
        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]
            self.max_heapify(largest)
        return self.list


if __name__ == '__main__':
    a = [16, 4, 10, 8, 7, 9, 3, 2, 4, 1]
    heapa = Heap(a)
    a = heapa.max_heapify(1)
    print(a)
