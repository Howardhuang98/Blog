# 进程的创建 create process
# LINUX 系统在os模块下的fork函数
from multiprocessing import Process
from time import sleep
import os


def task1():
    while True:
        sleep(1)
        print("sleep")


def task2():
    while True:
        sleep(2)
        print("do homework")


if __name__ == '__main__':
    print("父进程",os.getpid())
    P1 = Process(target=task1)

    P1.start()
    print(P1.pid)

    P2 = Process(target=task2)

    P2.start()
    print(P2.pid)
