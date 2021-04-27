class Solutions(object):
    def twoSum(self, nums, target):
        buffer_dict = {}
        for i,n in enumerate(nums):
            m = target -n
            if m in buffer_dict:
                return [buffer_dict[m],i]
            else:
                buffer_dict[n] = i