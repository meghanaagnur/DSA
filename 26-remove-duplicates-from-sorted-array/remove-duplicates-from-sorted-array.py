class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        j = 1
        while i < len(nums):
            if nums[i]==nums[i-1]:
                i += 1
            else:
                nums[j] = nums[i]
                j += 1
                i += 1
            
        return j