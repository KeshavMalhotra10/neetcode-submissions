class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {} #val : index

        for i, num in enumerate(nums):
            needed = target - num
            if needed in myHash:
                return [myHash[needed], i]
            myHash[num] = i
                