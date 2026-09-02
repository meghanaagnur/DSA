class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        numbers = {}
        for i in range(n):
            if nums[i] in numbers:
                index = numbers[nums[i]]
                if(abs(i-numbers[nums[i]])<=k):
                    return True
            numbers[nums[i]] = i
        return False
        

        