class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
    
        formatNums = sorted(set(nums))
        for num in nums:
            formatNums.append(num)
        #print(formatNums)
        consecNum = 1
        cur = 1
        for i in range(1, len(formatNums)):
            if formatNums[i] - 1 == formatNums[i-1]:
                cur+=1
                consecNum = max(cur, consecNum)
            else:
                cur = 1
        
        return consecNum
        
        
         
                


                
            


        