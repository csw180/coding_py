from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        max_length = 0
        for v in s :
            if  len(queue)==0 or v not in queue :
                queue.append(v)
            elif  v in queue :
                while (queue[0]!=v) :
                    queue.pop(0)
                queue.pop(0)
                queue.append(v)
            if  max_length < len(queue) :
                max_length = len(queue)
        return max_length



s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("dvdf"))
