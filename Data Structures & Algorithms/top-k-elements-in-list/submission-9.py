class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort solution
        res = []

        # created the frequencyDictionary
        freqDic = {}
        for num in nums:
            if num in freqDic:
                freqDic[num] += 1
            else:
                freqDic[num] = 1

        counts = {} #how to initialize this as an value of arrays
        for i in range(len(nums)+1):
            counts[i] = []

        #use bucket sort
        for key in freqDic:
            frequency = freqDic[key]
            counts[frequency].append(key)

        #finally take the top k values in counts in reverse until len(counts) = k
        for count in range(len(nums), 0, -1):
            for f in counts[count]:
                res.append(f)
                if len(res) == k:
                    return res



