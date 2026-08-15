class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myHash = {}
        res = []
        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in myHash:
                myHash[sortedWord].append(word)
            else:
                myHash[sortedWord] = []
                myHash[sortedWord].append(word)
        
        for key in myHash:
            res += [myHash[key]]
        return res
        
        
        