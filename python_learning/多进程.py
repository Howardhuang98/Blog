import multiprocessing
import datetime
import time


def task(t: int):
    print("this task will run {} second".format(t))
    time.sleep(t)
    return "result"


if __name__ == '__main__':
    # 实例化一个进程池
    start = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        # map 函数 用于启动函数
        res = pool.map(task, [1, 1, 1, 1, 1, 1])
        print(res)
    end = time.time()
    print("{} seconds used".format(end-start))
