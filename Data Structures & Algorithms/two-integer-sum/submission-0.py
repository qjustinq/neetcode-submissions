class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            new_num = target - nums[i]
            if new_num in seen:
                return [seen[new_num],i]

            seen[nums[i]] = i 
