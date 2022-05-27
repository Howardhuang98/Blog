---
fontfamilyoptions: UTF8
fontfamily: ctex
theme: Warsaw
title: 'Pandoc：将Markdown转为Beamer'
author: Huang Hao
institute: Tianjin University
---

# Pandoc：将Markdown转为Beamer

- Pandoc is a universal document converter! It is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library.

- Pandoc document: https://pandoc.org/#

- Here, I'll introduce how to convert my daily markdown notes into Beamer for weekly presentations. 

# General usage

`pandoc -f markdown -t beamer -o OutputFile -s InputFile`

- -o specified the output file;
- -s indicated outputting the completed file.

# Beamer structure

In default configure, every content under a first head (# first head) will be converted into one frame (slide).

Also, it can be customized by `--slide-level n`, where `n` is the level of heads. 

# Customize Your Beamer

Suggest to use meta-data that define in markdown. 

```yaml
---
fontfamilyoptions: UTF8
fontfamily: ctex
theme: Warsaw
title: 'this is a title'
subtitle: 'this is a subtitle'
author: Huang Hao
institute: Tianjin University
---
```

# Example

- one of list
- one of list

![image-20220527165419920](Pandoc%EF%BC%9A%E5%B0%86Markdown%E8%BD%AC%E4%B8%BABeamer.assets/image-20220527165419920.png)

Let's test a Figure.
$$
E=mc^2
$$
Also a Equation.

# Notifications

- When you are using Chinese in Beamer, make sure that: `\usepackage[UTF8]{ctex}`  and XeLaTeX compiler is used. 

- check the variables: pandoc -D beamer > template.txt. 

check out the result of this markdown file:

<object data="../Pandoc%EF%BC%9A%E5%B0%86Markdown%E8%BD%AC%E4%B8%BABeamer.assets/pdffile.pdf" type="application/pdf" width=800 height=800>
</object>



