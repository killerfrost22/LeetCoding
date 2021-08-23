class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = !nums.empty(); //When the array is empty, it's trivial. And if it's not empty, 
        for (int n : nums)  //i is just 1. So you can just let i = 1 and handle the trivial case as appropriate.
            if (n > nums[i-1])
                nums[i++] = n;
        return i;
    }
};