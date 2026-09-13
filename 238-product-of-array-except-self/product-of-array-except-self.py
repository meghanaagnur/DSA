class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        answer = [0] * n

        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for j in range(n-2,-1,-1):
            suff[j] = suff[j+1] * nums[j+1]

        for n in range(0,n):
            answer[n] = pref[n] * suff[n]
        
        return answer