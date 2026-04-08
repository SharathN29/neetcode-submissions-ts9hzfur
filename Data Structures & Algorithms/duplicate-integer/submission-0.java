class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> intSet = new HashSet();
        for (int n : nums) {
            if (intSet.contains(n)) {
                return true;
            }
            intSet.add(n);
        }
        return false;
    }
}
