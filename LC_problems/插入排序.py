"""
插入排序
"""


def insertion_sort(A: list):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

    return A


result = insertion_sort([1, 3, 2, 5, 7, 9])
print(result)

"""
重写插入排序使结果为升序
"""
def insertion_sort_reversed(a:list):
    for j in range(1,len(a)):
        key = a[j]
        i = j - 1
        while i>=0 and a[i]< key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key

    return a

result =  insertion_sort_reversed([31,41,59,26,41,58])
print(result)