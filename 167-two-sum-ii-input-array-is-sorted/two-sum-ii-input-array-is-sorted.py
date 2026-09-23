class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while(left < right):
            add = numbers [left] + numbers[right]
            if(add<target):
                left += 1
            elif(add>target):
                right -= 1
            else:
                number = [left + 1 , right + 1]
                return number