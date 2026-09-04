class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #save this for later i struggled on this
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            pointer_left = i + 1
            pointer_right = len(nums) - 1
            while pointer_left < pointer_right:
                current_sum = nums[i] + nums[pointer_right] + nums[pointer_left]
                if current_sum > 0:
                    pointer_right -= 1
                elif current_sum < 0:
                    pointer_left += 1
                else:
                    answer.append([nums[i],nums[pointer_left],nums[pointer_right]])
                    pointer_left += 1
                    while nums[pointer_left] == nums[pointer_left - 1] and pointer_left < pointer_right:
                        pointer_left += 1

        return answer

            
        