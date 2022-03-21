# html学习

h1-h6 六个标题标签

p标签 段落

a标签 超链接

img 图片标签

```html
<img src="" width=px/100% >
```

hr 水平分割线

ol 有序列表

​	<li> 	</li>

ul 无序列表

## 相对路径

../ 用于返回上一级目录

../../用于返回两级上级目录

## form 表单

用于提交表单

## 块级元素

行级元素 块级元素

h/p/div/ul/ol/table/form/hr

a/image/iframe/span

## 样式表

选择器

![img](htmlCSS.assets/632877C9-2462-41D6-BD0E-F7317E4C42AC.jpg)

### 标签选择器

h1 { }

### id选择器

HTML元素以id属性来设置id选择器,CSS 中 id 选择器以 "#" 来定义。

 ID属性不要以数字开头，数字开头的ID在 Mozilla/Firefox 浏览器中不起作用。

```
#para1
{
    text-align:center;
    color:red;
}
```

### class选择器

class 选择器用于描述一组元素的样式，class 选择器有别于id选择器，class可以在多个元素中使用。

class 选择器在HTML中以class属性表示, 在 CSS 中，类选择器以一个点"."号显示：

在以下的例子中，所有拥有 center 类的 HTML 元素均为居中。

```
.center {text-align:center;}
```

## CSS 样式

https://www.runoob.com/cssref/css-reference.html

### 内部样式表

<link rel="stylesheet" href=""> 外部样式表