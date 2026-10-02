class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        seen = {}
        right = 0
        while right<len(s):
            if s[right] in seen:
                while s[right] in seen:
                    seen.pop(s[left])
                    left += 1
            seen[s[right]] = True
            current_length = right- left + 1
            if max_length<current_length:
                max_length = current_length
            right += 1
        return max_length
