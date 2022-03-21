## python学习笔记

## 对象方法，类方法，静态方法


```python
class person:
    age = 18
    def __init__(self):
        self.name = 'jack'
    
    def say(self):
        print('***对象方法***')
        print('我今年',self.age)
    
    @classmethod   #写一个类方法用于在没有对象的时候更新age
    def update_age(cls):
        print('***类方法***')
        cls.age = 20
    @staticmethod #写一个静态方法来修改年龄
    def reduce_age():
        print('***静态方法***')
        person.age = 15
"""
总结：
对象方法：必须由对象调用，必须有一个self参数

类方法：可以直接由类调动

类方法与静态方法：注意装饰器。在定义时，类方法是有cls参数的，静态方法没有参数；对象是无法访问的。两者都可以在对象生成之前创建，因为类方法和静态方法都不依赖于对象。
"""    
```


```python
p = person()
p.say()
```

    ***对象方法***
    我今年 18

```python
person.update_age()
p = person()
p.say()
```

    ***类方法***
    ***对象方法***
    我今年 20

```python
person.reduce_age()
p = person()
p.say()
```

    ***静态方法***
    ***对象方法***
    我今年 15

## 魔术方法之 __init__

## 魔术方法之 new
```
class person:
    def __init__(self,name,age):
        print("***初始化***")
        self.name = name
        self.age = age
    """
    用init动态添加name和age两个属性
    

    """
    def __new__(cls,name,age):
        print("***申请内存，开辟空间***")
        position =  object.__new__(cls)
        print(position)
        return position
    """
    new功能就是在实例化时向内存申请地址
    """

```

```
p = person('jack',18)
```

    ***申请内存，开辟空间***
    <__main__.person object at 0x000001CE441AC0B8>
    ***初始化***

实例化时将调用这些方法（从类创建实例的过程称为实例化）。那就是您创建实例的时候。创建实例时将调用魔术方法__new__。使用此方法，您可以自定义实例创建。创建实例时，首先调用该方法，然后将调用__init__来初始化实例。

方法__new__将类引用作为第一个参数，然后是传递给构造函数的参数（传递给类的调用以创建实例的参数）。方法__new__负责创建实例，因此您可以使用此方法来自定义对象的创建。通常，方法__new__将返回创建的实例对象引用。一旦__new__方法完成执行，将调用__init__方法。

您可以通过使用super调用超类的__new__方法来创建该类的新实例。 像super（currentclass，cls）.__ new __（cls，[，…。]）之类的东西

您可以通过使用***super***函数或直接在***对象上***调用__new__方法来在__new__方法内部创建实例， *如果父类是object* ***。***那是，

***instance= super(MyClass，cls）.__ new __（cls，\* args，\** kwargs）***

要么

***instance=object.__ new __（cls，\* args，\*\* kwargs）***

## python中的hashable对象

An object is hashable if it has a hash value **which never changes** during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().


如果一个对象在自己的生命周期中有一哈希值（hash value）是不可改变的，那么它就是可哈希的（hashable）的，因为这些数据结构内置了哈希值，每个可哈希的对象都内置了__hash__方法，所以可哈希的对象可以通过哈希值进行对比，也可以作为字典的键值和作为set函数的参数。所有python中所有不可改变的的对象（imutable objects）都是可哈希的，比如字符串，元组，也就是说可改变的容器如字典，列表不可哈希（unhashable）。我们用户所定义的类的实例对象默认是可哈希的（hashable），它们都是唯一的，而hash值也就是它们的id()。
