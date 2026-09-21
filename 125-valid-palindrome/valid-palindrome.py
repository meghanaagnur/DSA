class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl = s.lower()
        left = 0
        right = len(sl)-1
        while left<right:
            while left<right and not sl[left].isalnum():
                left += 1
            while left<right and not sl[right].isalnum():
                right -= 1
            if(sl[left] == sl[right]):
                left += 1
                right -= 1
            else:
                return False
        return True