# Input: grades = [10,6,12,7,3,5]
# Output: 3
# Explanation: The following is a possible way to form 3 groups of students:
# - 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
# - 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
# - 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
# It can be shown that it is not possible to form more than 3 groups.

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        for i in range(len(grades)):
            if (i*(i+1)/2 > len(grades)):
                return i-1
        return 0
        