# 进程的创建 create process
# LINUX 系统在os模块下的fork函数
from multiprocessing import Process
from time import sleep
import os


def task1():
    while True:
        print("task1的PID是", os.getpid())
        sleep(1)
        print("sleep")


def task2():
    while True:
        print("task2的PID是", os.getpid())
        sleep(2)
        print("do homework")


if __name__ == '__main__':
    print("父进程的PID", os.getpid())

    P1 = Process(target=task1)
    P2 = Process(target=task2)
    P1.start()
    P2.start()
