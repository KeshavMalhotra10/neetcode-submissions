from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first sort the array
        res = []
        nums = sorted(nums)
        
        #make a frequency dictionary
        freqDic = {}
        for num in nums:
            if num in freqDic:
                freqDic[num] +=1
            else:
                freqDic[num] = 1
        
        #now we gotta somehow sort by frequency
        arr = []
        for num, count in freqDic.items():
            arr.append([count, num])
        sortedArr = sorted(arr)

        while len(res) != k:
            res.append(sortedArr.pop()[1])
        return res
        
    


        