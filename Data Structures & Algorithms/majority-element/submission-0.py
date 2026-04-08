class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_len = len(nums)
        majority_len = nums_len / 2

        items_count = {}

        for num in nums:
            if num in items_count:
                items_count[num] = items_count[num] + 1
            else:
                items_count[num] = 1
        
        for k in items_count.keys():
            if items_count[k] >= majority_len:
                return k
        
        return 0
        