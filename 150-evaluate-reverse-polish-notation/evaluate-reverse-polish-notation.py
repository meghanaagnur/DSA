class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            try:
                operand = int(i)
                stack.append(operand)
            except ValueError:
                operator = i
                a = stack.pop()
                b = stack.pop()
                if (operator == "+"):
                    result = a+b
                elif (operator == "*"):
                    result = a*b
                elif (operator == "/"):
                    result = int (b/a)
                else :
                    result = b - a
                stack.append(result)
        return stack[0]
        