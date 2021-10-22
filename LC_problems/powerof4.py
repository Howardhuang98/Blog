def isPowerOfFour(n):
    """
    4，16，64，256
    :type n: int
    :rtype: bool
    """
    while n>3:
        n = n/4
    if n == 1:
        return True
    else:
        return False

def isPowerOfFour1(n):
    """
    二进制写法
    1
    4：100
    16：2^4：10000
    64：01000000
    :param n:
    :return:
    """
    mask = 0xaaaaaaaa
    print(n&(n-1))# 是否为10000格式
    return n > 0 and (n & (n - 1)) == 0 and (n & mask) == 0


if __name__ == '__main__':
    print(isPowerOfFour(5))
    print(isPowerOfFour1(16))
