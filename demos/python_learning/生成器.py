"""
生成器就是带有yield的函数

"""


def func():
    for i in range(10):
        print("第{}次使用yield".format(i))
        yield i


def func2():
    i = 0
    while True:
        print("第{}次使用yield".format(i))
        yield i
        i += 1


next(func())
next(func())
next(func())

f = func2()
next(f)
next(f)
next(f)

# 注意差别
