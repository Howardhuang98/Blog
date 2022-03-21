# 文件的io

## open()

首先通过open函数打开一个文件，创建一个file对象

```
file object = open(file_name [, access_mode][, buffering])
```

文件名，可以是绝对路径

模式：

buffering寄存：不懂

![img](文件的io.assets/2112205-861c05b2bdbc9c28.png)

其中truncate代表是否覆盖

## file.close()

关闭文件是一个很好的习惯，当file对象被重新指定为另一个文件时也会自动关闭。

## file.write()

