#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6090.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/5 10:36  
------------      
"""
import collections
from typing import List


class TextEditor:

    def __init__(self):
        self.text = []
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.text += list(text)
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        self.text = self.text[:max(0, self.cursor - k)] + self.text[self.cursor:]
        old = self.cursor
        self.cursor = max(0, self.cursor - k)
        return old-self.cursor

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(self.cursor - k, 0)
        return "".join(self.text[max(self.cursor - 10, 0):self.cursor])

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.text), self.cursor + k)
        return "".join(self.text[max(self.cursor - 10, 0):self.cursor])


if __name__ == '__main__':
    t = TextEditor()
    t.addText("leetcode")
    print(t.deleteText(4))
    t.addText()
