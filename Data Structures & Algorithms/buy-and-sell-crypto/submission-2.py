class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start with a 2 item slider
        if len(prices) == 1:
            return 0
        left = 0
        right = 1
        maxVal = prices[right] - prices[left]
        
        while left!= len(prices) -1 and right!= len(prices) -1:
            if prices[left] > prices[right]:
                left = right
                right = right + 1
            else:
                right +=1
            newVal = prices[right] - prices[left]
            if newVal > maxVal:
                maxVal = newVal
        
        if maxVal > 0:
            return maxVal
        return 0
            

        