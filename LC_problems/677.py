#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   677.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/14 10:56  
------------      
"""


class TrieNode:
    """
    前缀树的链式存储
    """

    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key not in self.map:
            self.map.add(key)
            for char in key:
                i = ord(char) - ord('a')
                if node.next[i] is None:
                    node.next[i] = TrieNode()
                    node = node.next[i]
                    node.val += val
                else:
                    node = node.next[i]
                    node.val += val


    def sum(self, prefix: str) -> int:
        node = self.root
        ans = 0
        for char in prefix:
            i = ord(char) - ord('a')
            if node.next[i] is None:
                return 0
            else:
                node = node.next[i]
                ans = node.val
        return ans


if __name__ == '__main__':
    obj = MapSum()
    obj.insert("apple", 3)
    obj.insert("app", 2)
    obj.insert("apple", 2)
    print(obj.sum("ap"))
