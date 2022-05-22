from abc import ABC
from abc import abstractmethod

class estimator(ABC):
    """
    一个估计器抽象类
    """
    def show_name(self):
        print("我是一个估计器")

    @abstractmethod
    def run(self):
        """
        估计器运行方法
        """
    @abstractmethod
    def result(self):
        """
        结果展示
        """

class dynamic(estimator):

    def __init__(self):
        self.show_name()

    def run(self):
        print("运行中")

    def result(self):
        print("展示result")


d = dynamic()
d.run()