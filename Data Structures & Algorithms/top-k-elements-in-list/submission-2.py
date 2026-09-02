from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) #now we have a counted dictionary in descending order
        res = []
        #now simply output the first k keys of counts
        for i in range(k):
            res = [item[0] for item in counts.most_common(k)]
        return res



        