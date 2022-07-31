# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res += 1   
            temp = nums[i]
            for j in range(i, len(nums)):
                    nums[j] -= temp
            
        return res



# runtime = O (n log n)
# space = O (n^2)