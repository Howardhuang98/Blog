import threading
import time
"""
学习使用threading模块

"""

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("%s正在运行中......" % self.name)
        print("运行时间为{}".format(time.ctime()))
        time.sleep(10)

        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

        """

if __name__ == '__main__':
    for i in range(10):
        MyThread("第{}个线程".format(i)).start()
    print(threading.active_count())