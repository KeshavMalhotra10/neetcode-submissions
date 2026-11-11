class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedDic = {} #sorted string: string

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in groupedDic:
                groupedDic[sortedS] = []
            groupedDic[sortedS].append(s)
        return list(groupedDic.values())
            
            

            
        