class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #defined a dictionary
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in hashMap:
                return [hashMap[needed], i]
            hashMap[num] = i

            
            