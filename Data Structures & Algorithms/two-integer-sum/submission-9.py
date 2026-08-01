class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {} #value ->indice
        
        for i in range(len(nums)):
            value = nums[i]
            needed = target - value
            if needed in myHash:
                return [myHash[needed], i]
            else:
                myHash[value] = i
            


        
            
            