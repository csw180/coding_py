class Solution:
    def twoSum(self, nums, target: int) :
        for fidx in range(len(nums)-1) :
            for sidx in range(fidx+1,len(nums)) :
                print(fidx,sidx)
                if nums[fidx]+nums[sidx] == target :
                    return [fidx,sidx]

s = Solution()
print(s.twoSum([3,2,4],6))
