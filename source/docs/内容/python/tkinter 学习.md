# tkinter 学习

effbot.org/tkinterbook/

主窗口对象

TK()

```python
root=TK()
```

mainloop() 主循环



![image-20210526193258039](tkinter 学习.assets/image-20210526193258039.png)

![image-20210526193834580](tkinter 学习.assets/image-20210526193834580.png)

经典写法：

Frame 组件 用于放置其他组件，实现复杂的布局

![image-20210526201314970](tkinter 学习.assets/image-20210526201314970.png)





# Widget 

每个组件都有自己的参数，包括尺寸，内容等



对于label组件，他的参数（options）

![image-20210526201430141](tkinter 学习.assets/image-20210526201430141.png)

有三种定义方式：

1. 定义组件时传入
2. label.config()
3. 用字典索引，label["options"]=

# 布局管理器

pack 简单，要么竖直排列，要么水平排列

grid 网格排列

place 根据位置排列，像素位置

# 事件

![image-20210526204222318](tkinter 学习.assets/image-20210526204222318.png)

事件发生后会存储到event对象中：

![image-20210526204355112](tkinter 学习.assets/image-20210526204355112.png)

