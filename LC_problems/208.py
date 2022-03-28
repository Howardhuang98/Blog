#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   208.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/26 20:27  
------------      
"""
from collections import defaultdict
from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.children = defaultdict(lambda: None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self
        for ch in word:
            if not current.children[ch]:
                current.children[ch] = Trie()
            current = current.children[ch]
        current.isEnd = True
        return None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self
        for ch in word:
            if not current.children[ch]:
                return False
            current = current.children[ch]
        if current.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self
        for ch in prefix:
            if not current.children[ch]:
                return False
            current = current.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':

    obj = Trie()
    obj.insert('ab')
    print(obj.search('ab'))
    print(obj.search('a'))
    print(obj.search('ac'))
    print(obj.startsWith('abbb'))
