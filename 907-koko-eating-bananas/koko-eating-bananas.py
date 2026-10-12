class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        while(left<right):
            hour = 0
            k = (left + right)//2
            for i in piles:
                hour += ((i+k-1)//k)
            if hour<=h:
                right = k 
            else:
                left = k + 1
        return left