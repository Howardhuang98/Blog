from functools import partial
from multiprocessing import Pool


class school:

    def __init__(self):
        self.homework = []

    def run(self):
        with Pool(processes=2) as p:
            p.map(self.add,['1','1','2','3']) # self没进去

    def add(self,msg):
        self.homework.append(msg)
        print(msg)

if __name__ == '__main__':
    s = school()
    s.run()
    print(s.homework)
    partial()