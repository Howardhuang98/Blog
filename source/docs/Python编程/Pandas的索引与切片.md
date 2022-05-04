# Pandas的索引与切片

Pandas提供了多种索引模式与切片方法，因为常常混用，导致实际每次使用起来并不熟练，在此整理DataFrame的索引与切片方式，给出几种常用的切片方式。

> [官方教学](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)

## Label-based方法

1. 找某一列：`DataFrame.loc[:,'column0']`
2. 找某几列：`DataFrame.loc[:,['column0','column1','column2']]`
3. 找某一行：`DataFrame.loc['index',:]`
4. 找某几行：`DataFrame.loc[['index0','index1','index2'],:]`
5. 布尔索引：`DataFrame.loc[boolean expression]`

可见，`.loc`的功能非常强大，包括两种模式`.loc[[行],[列]]`，`.loc[布尔表达式]`

## Position-based方法

1. 找某一列：`DataFrame.iloc[:1]`
2. 找某几列：`DataFrame.iloc[:,[0,1,2]]`
3. 找某一行：`DataFrame.iloc[1,:]`
4. 找某几行：`DataFrame.iloc[[0,1,2],:]`
5. 布尔索引：`DataFrame.iloc[boolean expression]`

iloc是`.loc`的位置模式，只能依据位置（在DataFrame中并不显式存储）来索引，在使用中并不算常用。

## getitem方法

`[]`就是getitem方法，这个方法常常造成混淆。所以尽量避免使用。

`DataFrame['column0']`返回对应**列**的Series，这与Python直观的存储并不相符。

