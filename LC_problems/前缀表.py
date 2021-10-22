"""
给你一个下标从 0 开始的正整数数组 candiesCount ，其中 candiesCount[i] 表示你拥有的第 i 类糖果的数目。同时给你一个二维数组 queries ，其中 queries[i] = [favoriteTypei, favoriteDayi, dailyCapi] 。

你按照如下规则进行一场游戏：

你从第 0 天开始吃糖果。
你在吃完 所有 第 i - 1 类糖果之前，不能 吃任何一颗第 i 类糖果。
在吃完所有糖果之前，你必须每天 至少 吃 一颗 糖果。
请你构建一个布尔型数组 answer ，满足 answer.length == queries.length 。answer[i] 为 true 的条件是：在每天吃 不超过 dailyCapi 颗糖果的前提下，你可以在第 favoriteDayi 天吃到第 favoriteTypei 类糖果；否则 answer[i] 为 false 。注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。

请你返回得到的数组 answer 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def canEat(candiesCount: list, queries: list) -> list:
    preSum = [0] * (len(candiesCount) + 1)
    res = []
    for i in range(len(candiesCount)):
        preSum[i + 1] = preSum[i] + candiesCount[i]
    for candyType, day, cap in queries:
        min_cap, max_cap = day + 1, cap * (day + 1)
        first_candy, last_candy = preSum[candyType] + 1, preSum[candyType] + candiesCount[candyType]
        res.append(min_cap <= last_candy and max_cap >= first_candy)
    return res


if __name__ == '__main__':
    a = canEat([7, 4, 5, 3, 8],
               [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]])
    print(a)
