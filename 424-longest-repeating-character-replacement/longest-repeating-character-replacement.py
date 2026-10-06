class Solution(object): 
    def characterReplacement(self, s, k): 
        """ :type s: str
            :type k: int 
            :rtype: int """ 
        left=0 
        right= 0 
        max_substring = 0 
        count = {} 
        while(right<len(s)): 
            if s[right] in count:
                count[s[right]] += 1 
            else: 
                count[s[right]] = 1 
            most_freq = max(count.values()) 
            window = right - left + 1 
            while window-most_freq > k:
                count[s[left]] -= 1
                left += 1 
                most_freq = max(count.values()) 
                window = right - left + 1 
            max_substring = max(window,max_substring)
            right += 1 
        return max_substring