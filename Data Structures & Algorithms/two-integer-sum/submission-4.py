class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #Val: index

        for index, value in enumerate(nums):
            needed = target - value
            if needed in hashMap:
                return [hashMap[needed], index]
            hashMap[value] = index

        
                        