class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(s)
        tSorted = sorted(t)
        sSorted = ''.join(sSorted)
        tSorted = ''.join(tSorted)
        return sSorted == tSorted


        
        