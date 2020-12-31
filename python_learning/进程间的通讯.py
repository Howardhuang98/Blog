from multiprocessing import Queue, Process
from time import sleep


# Queue 是一个类，队列。 它有两个非常重要的方法：put() get()

# 假设我们现在在下载图片


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载", image)
        sleep(1)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功'.format(file))
        except:
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p2.start()
