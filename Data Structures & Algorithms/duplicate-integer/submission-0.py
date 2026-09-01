class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #So I think we first go through the list and turn it into a     dictionary 
        #Where we have the key as the number and its value as the number of time
        #it has appeared so we write a for loop too do that
        count = {}
        for i in nums:
            if i in count:
                return True
            else: 
                count[i] = 1

        return False

              