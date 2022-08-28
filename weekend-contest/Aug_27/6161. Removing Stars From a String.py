# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        count = 0
        for i in s.length()-1:
            if s.charAt(i) == '*':
                count+=1
            else:
                if count == 0:
                    res+=s.charAt(i)
                else:
                    count-=1

        ans = ""
        for j in res.length()-1:
            ans+=res.charAt(i)
            j-=1
        return ans

