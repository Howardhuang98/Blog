"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."
输出："We%20are%20happy."
"""

def solu(s:str)->str:
    result = []
    for i,char in enumerate(s):
        if char == ' ':
            result.append("%20")
        else:
            result.append(char)
    return ''.join(result)


result = solu("We are happy.")
print(result)