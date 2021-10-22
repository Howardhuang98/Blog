"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def titleToNumber(s: str) -> int:
    result = 0
    reversed_str = ''.join(reversed(s))

    for i,char in enumerate(reversed_str):
        # A 的ascii码为65
        result += (ord(char)-64) *26**i
    return result

print(titleToNumber('AB'))
