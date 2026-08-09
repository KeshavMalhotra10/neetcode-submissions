class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need a set
        #sliding window
        #track maxLength
        maxLength = 0
        mySet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l]) #if we find a duplicate then remove the leftmost character until no more duplicate (dasd -> asd)
                l+=1
            mySet.add(s[r])
            maxLength = max(maxLength, len(mySet))
        return maxLength




        
        
        

            
        