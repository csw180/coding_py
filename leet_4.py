from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merge_sorted = sorted(nums1)
        if len(merge_sorted)%2==0 :
            return (merge_sorted[(len(merge_sorted)//2) -1] + merge_sorted[len(merge_sorted)//2]) / 2
        else :
            return merge_sorted[len(merge_sorted)//2]

s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
print(s.findMedianSortedArrays([1,3],[2]))