class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDic = {}

        #sorted all strings found in the list and then add them to the dictionary
        #dictionary pairing: sorted string -> unsorted string

        for str in strs:
            strSorted = ''.join(sorted(str))

            if strSorted not in sortedDic:
                sortedDic[strSorted] = []
                sortedDic[strSorted].append(str)
            else:
                sortedDic[strSorted].append(str)
            
            modifiedList = []
            for key in sortedDic:
                modifiedList.append(sortedDic[key])
        
        return modifiedList

       
        

            
        

        