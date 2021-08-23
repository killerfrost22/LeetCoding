
class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int count = 0;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != nums[count]) {
                    count++;
                }else{
                    nums[i-count] = nums[i];
                }
            return nums-count;   
        }
    }