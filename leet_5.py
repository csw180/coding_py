from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for cnt in range(len(s),0,-1) :
            for i in range(len(s)-cnt+1) :
                t = s[i:i+cnt]
                # print(f'cnt={cnt},i={i},s={t},rev={t[::-1]}')
                if t == t[::-1] :
                    return t
        return ""


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("a"))
