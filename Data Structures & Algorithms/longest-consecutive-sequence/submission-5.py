class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_streak = 0
        num_set = set(nums)

        for i in num_set:
            if i-1 not in num_set:
                current_num = i
                counter = 1

                while current_num + 1 in num_set:
                    current_num +=1
                    counter += 1

                if counter > longest_streak:
                    longest_streak = counter

        return longest_streak


