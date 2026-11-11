class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myHash = {}

        for num in nums:
            if num in myHash:
                return True 
            myHash[num] = 1
        return False

        