class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left= 0
        right= len(nums)-1
        while (left<=right):
            middleind = left + ((right - left)//2)
            middle = nums[middleind]
            if(middle>target):
                right = middleind - 1
            elif (middle<target):
                left = middleind + 1
            else:
                return middleind
        return -1