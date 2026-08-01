class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        #if the number in hashset return true
        #else just continue and add to the hashset
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
        
        
        

        

