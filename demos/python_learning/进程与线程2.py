# 进程的创建 create process
# LINUX 系统在os模块下的fork函数
from multiprocessing import Process
from time import sleep
import os


# 自定义进程
class Myprocess(Process):
    def __init__(self, name):
        super(Myprocess,self).__init__()
        self.name = name


# 重写run方法
    def run(self):
        n = 1
        while True:
            sleep(1)
            # print ("进程名：",self.name)
            print("{}---------》自定义进程{}".format(n, self.name))
            n += 1


if __name__ == '__main__':
    p = Myprocess(name='小明')
    p.start()
    p1 = Myprocess(name='小红')
    p1.start()
