"""
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:

输入: [1, 2, 3, 4]

输出: False

解释: 序列中不存在132模式的子序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
# 这种解题太慢了
def find132pattern(nums: list) -> bool:
    i = 0
    j = 1
    k = 2
    while i < len(nums)-2:
        while j < len(nums)-1:
            while k <len(nums):
                if nums[i]<nums[k]<nums[j]:
                    return True
                else:
                    k += 1
            j += 1
            k = j+1
        i +=1
        j = i+1
        k = j+1
    return False

a =  [-1, 3, 2, 0]
print(find132pattern(a))


"""
先做一个min数组，满足min[j] = min(a[1 .. j])
"""
def find132pattern(nums) -> bool:
        le = len(nums)
        if le<2: return False

        mi = [nums[0]]
        for i in range(1, le):
            mi.append(min(nums[i], mi[-1]))
        
        stack = []
        for i in range(le-1, -1, -1):
            print(stack)
            if nums[i]>mi[i]:
                while stack and mi[i]>=stack[-1]:
                    stack.pop()
                
                if stack and stack[-1]<nums[i]:
                    return True
                stack.append(nums[i])
        return False

a =  [-1, 3, 2, 0]
print(find132pattern(a))
