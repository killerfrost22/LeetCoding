
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
                if stack and  stack[-1] == dict[char]: ## stack[-1] is the last value in the stack  
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False


# create a list of prime numbers
# prime_numbers = [2, 3, 5, 7]

# # remove the element at index 2
# removed_element = prime_numbers.pop(2)

# print('Removed Element:', removed_element)

# # Output: Removed Element: 5