# numpy 的数据存储与读取

https://numpy.org/doc/stable/reference/routines.io.html

常用的数据格式有：csv，txt，npy，npz。

将numpy转化为**二进制文件**或者**文本文件**，以此来持久化数据。

1. 将**一个**`array`存储为**一个**二进制文件；`numpy.save`

2. 将**多个**`array`存储为**一个**二进制文件；`numpy.savez`

3. 将一个array存储为文本文件；`numpy.savetxt`


读取numpy**二进制文件**，使用 `numpy.load`，读取**文本格式文件**，使用`numpy.loadtxt`
> 读取 .npz格式时，请使用上下文管理器

   

