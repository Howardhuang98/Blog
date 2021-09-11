def func(a,b,**kwargs):
    print(kwargs)
    return None


if __name__ == '__main__':
    a = {'a':1,'b':2,'key1':1,'key2':2}
    func(**a)

