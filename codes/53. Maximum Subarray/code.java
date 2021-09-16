import java.lang.Math;
class Solution {
    public int maxSubArray(int[] nums) {
        int Rmax = nums[0]; int now = nums[0];
        int length  = nums.length; 
        for(int i = 1; i< length; i++){
            Rmax = Math.max(Rmax+nums[i], nums[i]);
            now = Math.max(Rmax, now );
            }
        return now;
        }
}