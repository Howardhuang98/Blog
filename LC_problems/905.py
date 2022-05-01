from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while True:
            while left < len(nums) and nums[left] % 2 == 0:
                left += 1
            while right >= 0 and nums[right] % 2 != 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                break
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([0]))
