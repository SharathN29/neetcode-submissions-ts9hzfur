class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i in range(len(nums)):
            if target - nums[i] in num_index:
                return [num_index.get(target-nums[i]), i]
            else:
                num_index[nums[i]] = i
        return [-1, -1]
        