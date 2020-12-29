"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。


"""


def sortArrayByParityII(A: list) -> list:
    odd = []
    even = []
    result = []
    for a in A:
        # 如果是奇数
        if a % 2 == 1:
            odd.append(a)
        if a % 2 == 0:
            even.append(a)
    for i in range(len(odd)):
        result.append(even[i])
        result.append(odd[i])
    return result


print(sortArrayByParityII([2, 6, 8, 3, 10, 7, 9, 11]))
"""
双指针法

"""


def sortArrayByParityII(A: list) -> list:
    odd = 1
    even = 0
    while True:
        while even < len(A):

            if A[even] % 2 == 1:
                break
            if A[even] % 2 == 0:
                even += 2

        while odd < len(A):

            if A[odd] % 2 == 0:
                break
            if A[odd] % 2 == 1:
                odd += 2

        if even == len(A) :
            return A
        else:
            A[even], A[odd] = A[odd], A[even]


print(sortArrayByParityII([4, 1, 1, 0, 1, 0]))
