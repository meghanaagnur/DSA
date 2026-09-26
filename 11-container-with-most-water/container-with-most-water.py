class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while(left<right):
            width = right - left
            length = min(height[left],height[right])
            area = width * length
            if(area>max_area):
                max_area = area
            if(length == height[left]):
                left += 1
            else:
                right -= 1
        return max_area