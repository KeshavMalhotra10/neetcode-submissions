class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count frequencies
        freqMap = Counter(nums)
        

        #sort the frequency map by descending order
        freqMap = sorted(freqMap.items(), key = lambda item:item[1], reverse = True)

        #return the first k elements
        return [key for (key, _) in freqMap[:k]]
        