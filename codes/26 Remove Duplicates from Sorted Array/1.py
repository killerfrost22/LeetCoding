class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                res +=1
                nums[res] = nums[i]
        return res+1