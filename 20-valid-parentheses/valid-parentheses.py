class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =  []
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for i in s:
            if i not in pair:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif pair[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False