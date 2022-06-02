

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float("+inf") for i in s]
        index = [-1]
        for i,char in enumerate(s):
            if char == c:
                index.append(i)
        index.append(100000)
        for i,idx in enumerate(index):
            if i == 0 or i ==len(index)-1:
                continue
            left = idx-1
            right = idx
            while left>-1 and left>index[i-1]:
                if ans[left]>abs(left-idx):
                    ans[left] = abs(left-idx)
                    left -= 1
                else:
                    break
            while right<len(s) and right < index[i+1]:
                if ans[right]>abs(right-idx):
                    ans[right] = abs(right-idx)
                    right += 1
                else:
                    break
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar(s = "loveleetcode", c = "e"))
    print(s.shortestToChar(s = "aaab", c = "b"))