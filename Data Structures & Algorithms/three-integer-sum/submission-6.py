class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myHash = {} #value -> indice

        for i, num in enumerate(nums):
            myHash[num] = i

        res = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                needed = 0 - nums[i] - nums[j]
                if needed in myHash and myHash[needed] > j:
                    res.add(tuple(sorted((needed, nums[i], nums[j]))))
        return [list(t) for t in res]

                

        