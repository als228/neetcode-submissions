class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();
        for (int num : nums){
            if (numsMap.get(num) == null) numsMap.put(num, 1);
            else return true;
        }

        return false;
    }
}