#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   一年中的第几天.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/12/21 19:59  
------------      
"""
"""
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-year
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def dayOfYear(date: str) -> int:
    year = int(date[0:4])
    month = int(date[5: 7])
    day = int(date[8: 10])
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31,
        12: 30
    }
    if year % 400 == 0:
        days[2] += 1
    elif year % 4 == 0 and year % 100 != 0:
        days[2] += 1
    days = sum(days[i] for i in range(1, month))
    days += day
    return days

if __name__ == '__main__':
    dayOfYear("2012-01-02")
