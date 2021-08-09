
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack  = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict:
                if stack and  stack[-1] == dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False