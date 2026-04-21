class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> mp = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            mp.put(nums[i], i);
        }
        if (nums.length == mp.size()) return false;
        else return true;
    }
}