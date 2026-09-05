class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0
        pointer_left = 0
        pointer_right = 1
        while pointer_right < len(prices):
            if prices[pointer_left] > prices[pointer_right]:
                pointer_left = pointer_right
                pointer_right +=1
            else:
                current_profit = prices[pointer_right] - prices[pointer_left]
                print( prices[pointer_left] , prices[pointer_right])
                pointer_right +=1
                
            if current_profit > max_profit:
                max_profit = current_profit
            
        
        return max_profit

        
        