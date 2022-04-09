#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1604.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/9 13:10  
------------      
"""
from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        row_memo = [None for _ in range(len(board))]
        col_memo = [None for _ in range(len(board))]
        dia = [None, None]
        state = "Draw"
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    state = "Pending"
                if row_memo[i] and row_memo[i] != "L":
                    if row_memo[i] != board[i][j]:
                        row_memo[i] = "L"
                elif not row_memo[i]:
                    row_memo[i] = board[i][j]

                if col_memo[j] and col_memo[j] != "L":
                    if col_memo[j] != board[i][j]:
                        col_memo[j] = "L"
                elif not col_memo[j]:
                    col_memo[j] = board[i][j]

                if i == j:

                    if dia[0] and dia[0] != "L":
                        if dia[0] != board[i][j]:
                            dia[0] = "L"
                    elif not dia[0]:
                        dia[0] = board[i][j]

                if j == (len(board) - i-1):
                    if dia[1] and dia[1] != "L":
                        if dia[1] != board[i][j]:
                            dia[1] = "L"
                    elif not dia[1]:
                        dia[1] = board[i][j]

        nx = 0
        no = 0
        print(row_memo)
        print(col_memo)
        print(dia)
        for res in row_memo+col_memo+dia:
            if res == "X":
                nx += 1
            if res == "O":
                no += 1

        if nx==no:
            return state
        elif nx>no:
            return "X"
        else:
            return "O"

if __name__ == '__main__':
    s = Solution()
    print(s.tictactoe(["OOXXOXXX","XXXOXOXO","OXOXXXOO","XOXOXXXX","OXOOXOOO","XOOOOOOO","OXXXOOOX","XOXOOXXX"]))


