class Solution {
    public boolean hasDuplicate(int[] nums) {
        int arrLen = nums.length;
        if (arrLen == 0) {
            return false;
        }
        Set<Integer> duplicates = new HashSet();

        for (int i = 0; i < arrLen; i++) {
            if (duplicates.contains(nums[i])) {
                return true;
            }
            duplicates.add(nums[i]);
        }

        return false;
    }
}
