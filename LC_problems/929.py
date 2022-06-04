import re
from typing import List

from pip import main


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for s in emails:
            l = re.split("[\+.*]?@+",s)
            local = l[0]
            domain = l[1]
            ans.add("".join(local.split("."))+"@"+domain)
        return len(ans)
            

if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
    