class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0 
        maxSize = 0

        #initially we set our window to be just the first character

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            size = r -l + 1
            maxSize = max(size, maxSize)

        return maxSize
        






            
                    