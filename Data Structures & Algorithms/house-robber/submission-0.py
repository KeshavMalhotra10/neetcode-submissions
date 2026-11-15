class Solution:
    def rob(self, nums: List[int]) -> int:
        #1. Subpproblem: return max money from robbing houses best[i]
        #2. Reccurence: if we rob house[i], then best[i] = house[i] + house[i-2], if we rob house[i-1], best[i] = house[i-1] 
        #3. Basecase: you rob the first house, and second house
        if len(nums) == 1:
            return nums[0]
        best = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            best.append(max(best[i-2] + nums[i], best[i-1]))  
        return best[len(nums)-1]