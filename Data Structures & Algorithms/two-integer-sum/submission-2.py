class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_index:
                return [num_index.get(diff), i]
            else:
                num_index[nums[i]] = i
        return [-1, -1]
        