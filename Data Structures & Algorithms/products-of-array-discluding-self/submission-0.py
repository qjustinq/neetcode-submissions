class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        product = 1
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1,-1,-1):
            postfix.append(product)
            product *= nums[i]

        postfix.reverse()
        
        answer = []
        for i in range(len(nums)):
            answer.append(postfix[i] * prefix[i])

        return answer 
            