
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = re.fullmatch(p,s)
        return False if m is None else True

print(Solution().isMatch('aa','a'))