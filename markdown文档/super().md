# super()

https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

案例一，一个子类像扩展内建的类：

```python
class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)
```

这个类有父类的所有功能，它拓展了\__setitem__方法，可以看到，执行的时候，这个方法用super()来把工作分配到真正的增加键值对上去。

如果说，没有super(), 我们将写成：

```python
dict.__setitem__(self, key, value)
```

使用super()更好，因为他是一个计算好的间接引用。第一个好处就是，我们不用明确委派的类的名字，如果说你修改源码的时候，修改了继承类，super()会自动引用现在的基类。

```
class LoggingDict(SomeOtherMapping):            # new base class
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)         # no change needed
```

**所以好处一：isolating changes**



计算收到两方面影响：super() call来的类，实例的祖先树。前部分，super call来的类，是收到源码决定的，比如说我们的例子中，super是固定的，在\__setitem__方法中被调用。第二部分是更加灵活的，比如我们现在再创建一个类：

```
class LoggingOD(LoggingDict, collections.OrderedDict):
    pass
```

对于我们的新类来说，祖先树为

loggingOD -> loggingDict -> OrderedDict -> dict -> object

重要的结果是，OrderedDict被放在了loggingDict与dict之间，意味着\__setitem__中super()会调用OrderedDict 而不是 dict。

所以搜索顺序，对于super来说非常重要：也就是方法解析顺序 method resolution order MRO：

```
>>> pprint(LoggingOD.__mro__)
(<class '__main__.LoggingOD'>,
 <class '__main__.LoggingDict'>,
 <class 'collections.OrderedDict'>,
 <class 'dict'>,
 <class 'object'>)
```

在super机制里可以保证公共父类仅被执行一次，按照的就是MRO的顺序。